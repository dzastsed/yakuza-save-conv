import unittest
from unittest.mock import MagicMock, patch
from main import File


class TestFile(unittest.TestCase):
    def setUp(self):
        self.ui_instance = MagicMock()
        self.file_manager = File(self.ui_instance)

    @patch('main.filedialog.askopenfilename', return_value='')
    def test_no_ps3_input_chosen(self, mock_askopenfilename):
        self.file_manager.choose_ps3_input()
        self.assertEqual(getattr(self.file_manager, '_File__input_ps3'), [])
        self.assertFalse(self.ui_instance.lbl1.configure.called)

    @patch('main.filedialog.askopenfilename', return_value='')
    def test_no_pc_input_chosen(self, mock_askopenfilename):
        self.file_manager.choose_pc_input()
        self.assertEqual(getattr(self.file_manager, '_File__input_pc'), [])
        self.assertFalse(self.ui_instance.lbl2.configure.called)

    @patch('main.filedialog.askdirectory', return_value='')
    def test_no_output_chosen(self, mock_askdirectory):
        self.file_manager.choose_output()
        self.assertEqual(getattr(self.file_manager, '_File__output'), [])
        self.assertFalse(self.ui_instance.lbl3.configure.called)


if __name__ == '__main__':
    unittest.main()
