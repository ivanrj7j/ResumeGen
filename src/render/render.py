import os
import subprocess
from uuid import uuid4 as uuid
import shutil
from logging import Logger

class Renderer:
    def __init__(self, logger:Logger|None=None):
        """
        Initializes the Renderer instance.

        Args:
            logger (Logger | None, optional): An optional logger instance for logging output and errors. Defaults to None.
        """
        self.logger = logger

    def renderPDF(self, src:str, path:str=".", customName:str=""):
        """
        Compiles a LaTeX source file into a PDF using pdflatex. The generated PDF is moved to the specified output directory and can be renamed.

        For refernce: https://stackoverflow.com/questions/8085520/generating-pdf-latex-with-python-script

        Args:
            src (str): Path to the LaTeX source (.tex) file to be compiled.
            path (str, optional): Output directory for the generated PDF file. Defaults to current directory (".").
            customName (str, optional): Custom name for the output PDF file (with or without .pdf extension). If not provided, uses the source filename. Defaults to empty string.
        Raises:
            FileNotFoundError: If the specified source file does not exist.
        Returns:
            None
        Side Effects:
            - Creates a temporary directory for compilation.
            - Moves the generated PDF to the output directory.
            - Cleans up temporary files and directories.
            - Logs output and errors if a logger is provided.
        """
        if not os.path.exists(src):
            raise FileNotFoundError(f"The given file {src} does not exist")
        
        outputDir = self.__generateTemp()
        inputFile = os.path.basename(src)
        inputFileName = os.path.splitext(inputFile)[0]
        outputFile = f"{inputFileName}.pdf"
        outputSrc = os.path.join(outputDir, outputFile)
        outputDst = os.path.join(path, self.__getOuputFileName(outputFile, customName))

        command = ['pdflatex', '-interaction', 'nonstopmode', '-output-directory', outputDir, src]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        self.__moveOutput(outputSrc, outputDst)

        shutil.rmtree(outputDir)

        if isinstance(self.logger, Logger):
            for line in stderr.splitlines():
                self.logger.error(line.decode())
            for line in stdout.splitlines():
                self.logger.info(line.decode())
            self.logger.info("RENDER COMPLETE!")
        
    def __generateTemp(self):
        """
        Generates a unique temporary directory for storing intermediate compilation files.

        Returns:
            str: The name of the created temporary directory.
        Side Effects:
            - Creates a new directory in the current working directory.
        """
        name = f"temp{str(uuid())}"
        if os.path.exists(name):
            self.__generateTemp()
        os.mkdir(name)
        return name
    
    def __moveOutput(self, outputSrc, outputDst):
        """
        Moves the compiled PDF from the temporary directory to the desired output location. If a file already exists at the destination, it is removed first.

        Args:
            outputSrc (str): Path to the source PDF file.
            outputDst (str): Path to the destination PDF file.
        Returns:
            None
        Side Effects:
            - Removes existing file at destination if present.
            - Moves the file to the destination.
        """
        if os.path.exists(outputDst):
            os.remove(outputDst)
            self.__moveOutput(outputSrc, outputDst)
        else:
            os.rename(outputSrc, outputDst)

    def __getOuputFileName(self, default:str, preffered:str):
        """
        Determines the output PDF filename based on a preferred name or defaults to the original filename.

        Args:
            default (str): The default filename to use if no preferred name is provided.
            preffered (str): The preferred filename (with or without .pdf extension).
        Returns:
            str: The final output filename with .pdf extension.
        """
        if preffered is None or preffered == "":
            return default
        if "." not in preffered:
            return preffered + ".pdf"
        return preffered