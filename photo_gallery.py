
import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QGridLayout, QLabel, QFileDialog, QLineEdit, 
                            QComboBox, QSlider, QMenuBar, QMenu, QScrollArea, QStatusBar, 
                            QDialog, QFormLayout, QSpinBox, QCheckBox, QToolBar, QMessageBox)
from PyQt6.QtGui import QPixmap, QImage, QIcon, QFont, QPalette, QColor, QAction
from PyQt6.QtCore import Qt, QSize, QTimer
from PIL import Image
import json
import uuid
from datetime import datetime
import shutil
from pathlib import Path

class LanguageManager:
    def __init__(self):
        self.translations = {
            'en': {
                'title': 'Photo Gallery',
                'open_folder': 'Open Folder',
                'search': 'Search',
                'add_tag': 'Add Tag',
                'slideshow': 'Slideshow',
                'edit': 'Edit',
                'rotate_left': 'Rotate Left',
                'rotate_right': 'Rotate Right',
                'crop': 'Crop',
                'save': 'Save',
                'cancel': 'Cancel',
                'language': 'Language',
                'theme': 'Theme',
                'default_theme': 'Default',
                'light_theme': 'Light',
                'dark_theme': 'Dark',
                'red_theme': 'Red',
                'blue_theme': 'Blue',
                'no_images': 'No images found in the selected folder.',
                'tag_placeholder': 'Enter tag...',
                'search_placeholder': 'Search images...',
                'crop_dialog': 'Crop Image',
                'width': 'Width',
                'height': 'Height',
                'x_pos': 'X Position',
                'y_pos': 'Y Position',
                'apply': 'Apply',
                'file_menu': 'File',
                'exit': 'Exit',
                'view_menu': 'View',
                'about': 'About',
                'about_text': 'Photo Gallery Application\nVersion 1.0\nDeveloped with PyQt6 and Pillow'
            },
            'fa': {
                'title': 'گالری تصاویر',
                'open_folder': 'باز کردن پوشه',
                'search': 'جستجو',
                'add_tag': 'افزودن برچسب',
                'slideshow': 'نمایش اسلاید',
                'edit': 'ویرایش',
                'rotate_left': 'چرخش به چپ',
                'rotate_right': 'چرخش به راست',
                'crop': 'برش',
                'save': 'ذخیره',
                'cancel': 'لغو',
                'language': 'زبان',
                'theme': 'تم',
                'default_theme': 'پیش‌فرض',
                'light_theme': 'روشن',
                'dark_theme': 'تیره',
                'red_theme': 'قرمز',
                'blue_theme': 'آبی',
                'no_images': 'هیچ تصویری در پوشه انتخاب شده یافت نشد.',
                'tag_placeholder': 'برچسب را وارد کنید...',
                'search_placeholder': 'جستجوی تصاویر...',
                'crop_dialog': 'برش تصویر',
                'width': 'عرض',
                'height': 'ارتفاع',
                'x_pos': 'موقعیت X',
                'y_pos': 'موقعیت Y',
                'apply': 'اعمال',
                'file_menu': 'فایل',
                'exit': 'خروج',
                'view_menu': 'نمایش',
                'about': 'درباره',
                'about_text': 'برنامه گالری تصاویر\nنسخه ۱.۰\nتوسعه یافته با PyQt6 و Pillow'
            },
            'zh': {
                'title': '图片库',
                'open_folder': '打开文件夹',
                'search': '搜索',
                'add_tag': '添加标签',
                'slideshow': '幻灯片',
                'edit': '编辑',
                'rotate_left': '向左旋转',
                'rotate_right': '向右旋转',
                'crop': '裁剪',
                'save': '保存',
                'cancel': '取消',
                'language': '语言',
                'theme': '主题',
                'default_theme': '默认',
                'light_theme': '浅色',
                'dark_theme': '深色',
                'red_theme': '红色',
                'blue_theme': '蓝色',
                'no_images': '在选定文件夹中未找到图片。',
                'tag_placeholder': '输入标签...',
                'search_placeholder': '搜索图片...',
                'crop_dialog': '裁剪图片',
                'width': '宽度',
                'height': '高度',
                'x_pos': 'X位置',
                'y_pos': 'Y位置',
                'apply': '应用',
                'file_menu': '文件',
                'exit': '退出',
                'view_menu': '视图',
                'about': '关于',
                'about_text': '图片库应用程序\n版本1.0\n使用PyQt6和Pillow开发'
            },
            'ru': {
                'title': 'Фотогалерея',
                'open_folder': 'Открыть папку',
                'search': 'Поиск',
                'add_tag': 'Добавить тег',
                'slideshow': 'Слайд-шоу',
                'edit': 'Редактировать',
                'rotate_left': 'Повернуть влево',
                'rotate_right': 'Повернуть вправо',
                'crop': 'Обрезать',
                'save': 'Сохранить',
                'cancel': 'Отмена',
                'language': 'Язык',
                'theme': 'Тема',
                'default_theme': 'По умолчанию',
                'light_theme': 'Светлая',
                'dark_theme': 'Темная',
                'red_theme': 'Красная',
                'blue_theme': 'Синяя',
                'no_images': 'В выбранной папке не найдено изображений.',
                'tag_placeholder': 'Введите тег...',
                'search_placeholder': 'Поиск изображений...',
                'crop_dialog': 'Обрезка изображения',
                'width': 'Ширина',
                'height': 'Высота',
                'x_pos': 'Позиция X',
                'y_pos': 'Позиция Y',
                'apply': 'Применить',
                'file_menu': 'Файл',
                'exit': 'Выход',
                'view_menu': 'Вид',
                'about': 'О программе',
                'about_text': 'Приложение фотогалереи\nВерсия 1.0\nРазработано с использованием PyQt6 и Pillow'
            }
        }
        self.current_language = 'en'

    def get(self, key):
        return self.translations[self.current_language].get(key, key)

    def set_language(self, lang):
        self.current_language = lang

class ThemeManager:
    def __init__(self, app):
        self.app = app
        self.themes = {
            'default': {
                'background': QColor(240, 240, 240),
                'foreground': QColor(0, 0, 0),
                'button': QColor(225, 225, 225),
                'button_text': QColor(0, 0, 0),
                'highlight': QColor(0, 120, 215),
            },
            'light': {
                'background': QColor(255, 255, 255),
                'foreground': QColor(0, 0, 0),
                'button': QColor(240, 240, 240),
                'button_text': QColor(0, 0, 0),
                'highlight': QColor(0, 120, 215),
            },
            'dark': {
                'background': QColor(30, 30, 30),
                'foreground': QColor(255, 255, 255),
                'button': QColor(60, 60, 60),
                'button_text': QColor(255, 255, 255),
                'highlight': QColor(0, 120, 215),
            },
            'red': {
                'background': QColor(50, 0, 0),
                'foreground': QColor(255, 255, 255),
                'button': QColor(100, 0, 0),
                'button_text': QColor(255, 255, 255),
                'highlight': QColor(200, 0, 0),
            },
            'blue': {
                'background': QColor(0, 0, 50),
                'foreground': QColor(255, 255, 255),
                'button': QColor(0, 0, 100),
                'button_text': QColor(255, 255, 255),
                'highlight': QColor(0, 0, 200),
            }
        }
        self.current_theme = 'default'

    def apply_theme(self, theme_name):
        self.current_theme = theme_name
        palette = QPalette()
        theme = self.themes[theme_name]
        palette.setColor(QPalette.ColorRole.Window, theme['background'])
        palette.setColor(QPalette.ColorRole.WindowText, theme['foreground'])
        palette.setColor(QPalette.ColorRole.Button, theme['button'])
        palette.setColor(QPalette.ColorRole.ButtonText, theme['button_text'])
        palette.setColor(QPalette.ColorRole.Highlight, theme['highlight'])
        self.app.setPalette(palette)

class CropDialog(QDialog):
    def __init__(self, parent, image_path, lang_manager):
        super().__init__(parent)
        self.lang_manager = lang_manager
        self.image_path = image_path
        self.setWindowTitle(self.lang_manager.get('crop_dialog'))
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()
        self.width_spin = QSpinBox()
        self.height_spin = QSpinBox()
        self.x_spin = QSpinBox()
        self.y_spin = QSpinBox()

        self.width_spin.setRange(1, 10000)
        self.height_spin.setRange(1, 10000)
        self.x_spin.setRange(0, 10000)
        self.y_spin.setRange(0, 10000)

        layout.addRow(self.lang_manager.get('width'), self.width_spin)
        layout.addRow(self.lang_manager.get('height'), self.height_spin)
        layout.addRow(self.lang_manager.get('x_pos'), self.x_spin)
        layout.addRow(self.lang_manager.get('y_pos'), self.y_spin)

        buttons = QHBoxLayout()
        apply_btn = QPushButton(self.lang_manager.get('apply'))
        cancel_btn = QPushButton(self.lang_manager.get('cancel'))
        apply_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        buttons.addWidget(apply_btn)
        buttons.addWidget(cancel_btn)

        layout.addRow(buttons)
        self.setLayout(layout)

    def get_crop_params(self):
        return {
            'width': self.width_spin.value(),
            'height': self.height_spin.value(),
            'x': self.x_spin.value(),
            'y': self.y_spin.value()
        }

class ImageWidget(QWidget):
    def __init__(self, image_path, lang_manager):
        super().__init__()
        self.image_path = image_path
        self.lang_manager = lang_manager
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.image_label = QLabel()
        self.load_image()
        layout.addWidget(self.image_label)
        
        self.tag_label = QLabel()
        self.tag_label.setWordWrap(True)
        layout.addWidget(self.tag_label)
        
        self.setLayout(layout)

    def load_image(self):
        pixmap = QPixmap(self.image_path)
        scaled_pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, 
                                    Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        self.load_tags()

    def load_tags(self):
        tag_file = self.image_path + '.tags'
        tags = []
        if os.path.exists(tag_file):
            with open(tag_file, 'r') as f:
                tags = json.load(f).get('tags', [])
        self.tag_label.setText(', '.join(tags) if tags else self.lang_manager.get('no_tags'))

class PhotoGallery(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang_manager = LanguageManager()
        self.theme_manager = ThemeManager(QApplication.instance())
        self.image_paths = []
        self.current_folder = ''
        self.slideshow_timer = QTimer()
        self.slideshow_index = 0
        self.init_ui()
        self.load_settings()
        self.apply_direction()

    def init_ui(self):
        # Window setup
        self.setWindowTitle(self.lang_manager.get('title'))
        self.setGeometry(100, 100, 1200, 800)
        self.setWindowIcon(QIcon('gallery_icon.png'))

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu(self.lang_manager.get('file_menu'))
        open_action = QAction(self.lang_manager.get('open_folder'), self)
        open_action.triggered.connect(self.open_folder)
        file_menu.addAction(open_action)
        exit_action = QAction(self.lang_manager.get('exit'), self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        view_menu = menubar.addMenu(self.lang_manager.get('view_menu'))
        about_action = QAction(self.lang_manager.get('about'), self)
        about_action.triggered.connect(self.show_about)
        view_menu.addAction(about_action)

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        language_combo = QComboBox()
        language_combo.addItems(['English', 'فارسی', '中文', 'Русский'])
        language_combo.currentIndexChanged.connect(self.change_language)
        toolbar.addWidget(QLabel(self.lang_manager.get('language') + ': '))
        toolbar.addWidget(language_combo)

        theme_combo = QComboBox()
        theme_combo.addItems([
            self.lang_manager.get('default_theme'),
            self.lang_manager.get('light_theme'),
            self.lang_manager.get('dark_theme'),
            self.lang_manager.get('red_theme'),
            self.lang_manager.get('blue_theme')
        ])
        theme_combo.currentIndexChanged.connect(self.change_theme)
        toolbar.addWidget(QLabel(self.lang_manager.get('theme') + ': '))
        toolbar.addWidget(theme_combo)

        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Control panel
        control_panel = QHBoxLayout()
        open_btn = QPushButton(self.lang_manager.get('open_folder'))
        open_btn.clicked.connect(self.open_folder)
        control_panel.addWidget(open_btn)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(self.lang_manager.get('search_placeholder'))
        self.search_input.textChanged.connect(self.search_images)
        control_panel.addWidget(self.search_input)

        tag_input = QLineEdit()
        tag_input.setPlaceholderText(self.lang_manager.get('tag_placeholder'))
        tag_input.returnPressed.connect(self.add_tag)
        control_panel.addWidget(tag_input)

        slideshow_btn = QPushButton(self.lang_manager.get('slideshow'))
        slideshow_btn.clicked.connect(self.start_slideshow)
        control_panel.addWidget(slideshow_btn)

        main_layout.addLayout(control_panel)

        # Image grid
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.scroll_area.setWidget(self.grid_widget)
        main_layout.addWidget(self.scroll_area)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Slideshow widget
        self.slideshow_widget = QWidget()
        self.slideshow_layout = QVBoxLayout(self.slideshow_widget)
        self.slideshow_image = QLabel()
        self.slideshow_layout.addWidget(self.slideshow_image)
        self.slideshow_controls = QHBoxLayout()
        prev_btn = QPushButton('◄')
        prev_btn.clicked.connect(self.prev_slide)
        next_btn = QPushButton('►')
        next_btn.clicked.connect(self.next_slide)
        stop_btn = QPushButton(self.lang_manager.get('cancel'))
        stop_btn.clicked.connect(self.stop_slideshow)
        self.slideshow_controls.addWidget(prev_btn)
        self.slideshow_controls.addWidget(next_btn)
        self.slideshow_controls.addWidget(stop_btn)
        self.slideshow_layout.addLayout(self.slideshow_controls)
        self.slideshow_widget.hide()

        # Context menu
        self.grid_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.grid_widget.customContextMenuRequested.connect(self.show_context_menu)

        # Slideshow timer
        self.slideshow_timer.timeout.connect(self.next_slide)

    def apply_direction(self):
        direction = Qt.LayoutDirection.RightToLeft if self.lang_manager.current_language == 'fa' else Qt.LayoutDirection.LeftToRight
        QApplication.instance().setLayoutDirection(direction)
        self.update_ui_text()

    def update_ui_text(self):
        self.setWindowTitle(self.lang_manager.get('title'))
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, ImageWidget):
                widget.load_tags()

    def change_language(self, index):
        lang_map = {0: 'en', 1: 'fa', 2: 'zh', 3: 'ru'}
        self.lang_manager.set_language(lang_map[index])
        self.apply_direction()
        self.save_settings()

    def change_theme(self, index):
        theme_map = {0: 'default', 1: 'light', 2: 'dark', 3: 'red', 4: 'blue'}
        self.theme_manager.apply_theme(theme_map[index])
        self.save_settings()

    def open_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.lang_manager.get('open_folder'))
        if folder:
            self.current_folder = folder
            self.load_images()

    def load_images(self):
        self.image_paths = []
        for ext in ('*.jpg', '*.jpeg', '*.png', '*.bmp'):
            self.image_paths.extend(Path(self.current_folder).glob(ext))
        
        for i in range(self.grid_layout.count()):
            self.grid_layout.itemAt(i).widget().deleteLater()
        
        if not self.image_paths:
            QMessageBox.information(self, self.lang_manager.get('title'), 
                                  self.lang_manager.get('no_images'))
            return

        row = col = 0
        for path in self.image_paths:
            image_widget = ImageWidget(str(path), self.lang_manager)
            self.grid_layout.addWidget(image_widget, row, col)
            col += 1
            if col >= 4:
                col = 0
                row += 1

    def search_images(self):
        search_text = self.search_input.text().lower()
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, ImageWidget):
                tags_file = widget.image_path + '.tags'
                visible = True
                if search_text:
                    if os.path.exists(tags_file):
                        with open(tags_file, 'r') as f:
                            tags = json.load(f).get('tags', [])
                        visible = any(search_text in tag.lower() for tag in tags)
                    else:
                        visible = False
                widget.setVisible(visible)

    def add_tag(self):
        sender = self.sender()
        tag = sender.text()
        if not tag:
            return

        selected_widget = None
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if widget.underMouse():
                selected_widget = widget
                break

        if selected_widget:
            tag_file = selected_widget.image_path + '.tags'
            tags = {'tags': []}
            if os.path.exists(tag_file):
                with open(tag_file, 'r') as f:
                    tags = json.load(f)
            if tag not in tags['tags']:
                tags['tags'].append(tag)
                with open(tag_file, 'w') as f:
                    json.dump(tags, f)
            selected_widget.load_tags()
            sender.clear()

    def show_context_menu(self, pos):
        widget = self.sender().childAt(pos)
        if not isinstance(widget, ImageWidget):
            return

        menu = QMenu()
        edit_menu = menu.addMenu(self.lang_manager.get('edit'))
        rotate_left = QAction(self.lang_manager.get('rotate_left'), self)
        rotate_right = QAction(self.lang_manager.get('rotate_right'), self)
        crop = QAction(self.lang_manager.get('crop'), self)
        
        rotate_left.triggered.connect(lambda: self.rotate_image(widget.image_path, -90))
        rotate_right.triggered.connect(lambda: self.rotate_image(widget.image_path, 90))
        crop.triggered.connect(lambda: self.crop_image(widget.image_path))
        
        edit_menu.addAction(rotate_left)
        edit_menu.addAction(rotate_right)
        edit_menu.addAction(crop)
        menu.exec(self.sender().mapToGlobal(pos))

    def rotate_image(self, image_path, angle):
        image = Image.open(image_path)
        rotated = image.rotate(angle, expand=True)
        rotated.save(image_path)
        for i in range(self.grid_layout.count()):
            widget = self.grid_layout.itemAt(i).widget()
            if isinstance(widget, ImageWidget) and widget.image_path == image_path:
                widget.load_image()
                break

    def crop_image(self, image_path):
        dialog = CropDialog(self, image_path, self.lang_manager)
        if dialog.exec():
            params = dialog.get_crop_params()
            image = Image.open(image_path)
            box = (params['x'], params['y'], 
                   params['x'] + params['width'], 
                   params['y'] + params['height'])
            cropped = image.crop(box)
            cropped.save(image_path)
            for i in range(self.grid_layout.count()):
                widget = self.grid_layout.itemAt(i).widget()
                if isinstance(widget, ImageWidget) and widget.image_path == image_path:
                    widget.load_image()
                    break

    def start_slideshow(self):
        if not self.image_paths:
            return
        self.centralWidget().hide()
        self.setCentralWidget(self.slideshow_widget)
        self.slideshow_widget.show()
        self.slideshow_index = 0
        self.show_slide()
        self.slideshow_timer.start(3000)

    def stop_slideshow(self):
        self.slideshow_timer.stop()
        self.slideshow_widget.hide()
        self.setCentralWidget(self.centralWidget())
        self.centralWidget().show()

    def show_slide(self):
        if self.image_paths:
            pixmap = QPixmap(str(self.image_paths[self.slideshow_index]))
            scaled = pixmap.scaled(self.slideshow_image.size(), 
                                 Qt.AspectRatioMode.KeepAspectRatio,
                                 Qt.TransformationMode.SmoothTransformation)
            self.slideshow_image.setPixmap(scaled)

    def next_slide(self):
        if self.image_paths:
            self.slideshow_index = (self.slideshow_index + 1) % len(self.image_paths)
            self.show_slide()

    def prev_slide(self):
        if self.image_paths:
            self.slideshow_index = (self.slideshow_index - 1) % len(self.image_paths)
            self.show_slide()

    def show_about(self):
        QMessageBox.information(self, self.lang_manager.get('about'), 
                              self.lang_manager.get('about_text'))

    def save_settings(self):
        settings = {
            'language': self.lang_manager.current_language,
            'theme': self.theme_manager.current_theme
        }
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

    def load_settings(self):
        try:
            with open('settings.json', 'r') as f:
                settings = json.load(f)
                self.lang_manager.set_language(settings.get('language', 'en'))
                self.theme_manager.apply_theme(settings.get('theme', 'default'))
                self.apply_direction()
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')  # Use generic Windows style for compatibility
    font = QFont('Segoe UI', 10)
    app.setFont(font)
    gallery = PhotoGallery()
    gallery.show()
    sys.exit(app.exec())
