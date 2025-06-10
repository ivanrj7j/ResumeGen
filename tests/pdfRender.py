import unittest
import os
import shutil
from src.render import Renderer
import logging

class TestRenderer(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("TestRenderer")
        self.logger.addHandler(logging.NullHandler())
        self.renderer = Renderer(self.logger)
        self.test_dir = "texSource"
        self.test_tex = os.path.join(self.test_dir, "test1.tex")
        self.output_pdf = os.path.join(self.test_dir, "test_output.pdf")
        self.custom_pdf = os.path.join(self.test_dir, "custom_name.pdf")
        # Clean up before test
        for f in [self.output_pdf, self.custom_pdf]:
            if os.path.exists(f):
                os.remove(f)

    def tearDown(self):
        # Clean up after test
        for f in [self.output_pdf, self.custom_pdf]:
            if os.path.exists(f):
                os.remove(f)

    def test_renderPDF_default_name(self):
        self.renderer.renderPDF(self.test_tex, self.test_dir, "test_output.pdf")
        self.assertTrue(os.path.exists(self.output_pdf))

    def test_renderPDF_custom_name(self):
        self.renderer.renderPDF(self.test_tex, self.test_dir, "custom_name")
        self.assertTrue(os.path.exists(self.custom_pdf))

    def test_renderFromSourceCode(self):
        with open(self.test_tex, encoding='utf-8') as f:
            tex_source = f.read()
        self.renderer.renderFromSourceCode(tex_source, self.test_dir, "custom_name.pdf")
        self.assertTrue(os.path.exists(self.custom_pdf))

    def test_renderPDF_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.renderer.renderPDF("nonexistent.tex", self.test_dir)

if __name__ == "__main__":
    unittest.main()

