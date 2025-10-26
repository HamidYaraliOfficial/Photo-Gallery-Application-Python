# Photo Gallery Application

## English

### Overview
The Photo Gallery Application is a desktop application built using Python, PyQt6, and Pillow. It allows users to browse, manage, and edit images in a selected folder. The application supports multiple languages, customizable themes, and provides features such as image tagging, slideshow viewing, and basic image editing capabilities like rotation and cropping.

### Features
- **Image Browsing**: Load and display images from a selected folder in a grid layout.
- **Tagging System**: Add and search for tags associated with images for easy organization.
- **Slideshow Mode**: View images in a slideshow with navigation controls.
- **Image Editing**: Rotate images left or right and crop images with customizable parameters.
- **Multilingual Support**: Available in English, Persian, Chinese, and Russian.
- **Theming**: Choose from default, light, dark, red, and blue themes for a personalized experience.
- **Settings Persistence**: Save language and theme preferences for future sessions.

### Requirements
- Python 3.9 or higher
- PyQt6
- Pillow (PIL)

### Installation
1. Ensure Python 3.9+ is installed on your system.
2. Install the required dependencies:
   ```bash
   pip install PyQt6 Pillow
   ```
3. Download the `photo_gallery.py` file from the repository.
4. Run the application:
   ```bash
   python photo_gallery.py
   ```

### Usage
1. Launch the application using the command above.
2. Use the "Open Folder" button or menu to select a directory containing images.
3. Add tags to images by typing in the tag input field and pressing Enter.
4. Search for images by entering tags in the search bar.
5. Start a slideshow using the "Slideshow" button.
6. Right-click on an image to access editing options (rotate, crop).
7. Change language or theme via the toolbar dropdown menus.
8. View application information through the "About" menu.

### Project Structure
- `photo_gallery.py`: Main application file containing all the logic and UI implementation.
- `settings.json`: Stores user preferences for language and theme (generated automatically).

### Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Ensure your code follows the project's coding style and includes appropriate documentation.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## فارسی

### نمای کلی
برنامه گالری تصاویر یک برنامه دسکتاپ است که با استفاده از پایتون، PyQt6 و Pillow ساخته شده است. این برنامه به کاربران امکان می‌دهد تصاویر موجود در یک پوشه انتخاب‌شده را مرور، مدیریت و ویرایش کنند. این برنامه از چندین زبان، تم‌های قابل تنظیم و قابلیت‌هایی مانند برچسب‌گذاری تصاویر، نمایش اسلاید و ویرایش پایه تصاویر مانند چرخش و برش پشتیبانی می‌کند.

### ویژگی‌ها
- **مرور تصاویر**: بارگذاری و نمایش تصاویر از یک پوشه انتخاب‌شده در یک چیدمان شبکه‌ای.
- **سیستم برچسب‌گذاری**: افزودن و جستجوی برچسب‌های مرتبط با تصاویر برای سازماندهی آسان.
- **حالت نمایش اسلاید**: مشاهده تصاویر در یک نمایش اسلاید با کنترل‌های ناوبری.
- **ویرایش تصویر**: چرخش تصاویر به چپ یا راست و برش تصاویر با پارامترهای قابل تنظیم.
- **پشتیبانی چندزبانه**: در دسترس به زبان‌های انگلیسی، فارسی، چینی و روسی.
- **تم‌سازی**: انتخاب از تم‌های پیش‌فرض، روشن، تیره، قرمز و آبی برای تجربه‌ای شخصی‌سازی‌شده.
- **پایداری تنظیمات**: ذخیره تنظیمات زبان و تم برای جلسات بعدی.

### پیش‌نیازها
- پایتون ۳.۹ یا بالاتر
- PyQt6
- Pillow (PIL)

### نصب
1. اطمینان حاصل کنید که پایتون ۳.۹ یا بالاتر روی سیستم شما نصب است.
2. وابستگی‌های مورد نیاز را نصب کنید:
   ```bash
   pip install PyQt6 Pillow
   ```
3. فایل `photo_gallery.py` را از مخزن دانلود کنید.
4. برنامه را اجرا کنید:
   ```bash
   python photo_gallery.py
   ```

### استفاده
1. برنامه را با استفاده از دستور بالا راه‌اندازی کنید.
2. از دکمه یا منوی «باز کردن پوشه» برای انتخاب پوشه‌ای حاوی تصاویر استفاده کنید.
3. با تایپ در فیلد ورودی برچسب و زدن Enter، برچسب‌ها را به تصاویر اضافه کنید.
4. با وارد کردن برچسب‌ها در نوار جستجو، تصاویر را جستجو کنید.
5. با استفاده از دکمه «نمایش اسلاید» اسلایدشو را شروع کنید.
6. روی یک تصویر راست‌کلیک کنید تا به گزینه‌های ویرایش (چرخش، برش) دسترسی پیدا کنید.
7. زبان یا تم را از طریق منوهای کشویی نوار ابزار تغییر دهید.
8. اطلاعات برنامه را از طریق منوی «درباره» مشاهده کنید.

### ساختار پروژه
- `photo_gallery.py`: فایل اصلی برنامه که شامل تمام منطق و پیاده‌سازی رابط کاربری است.
- `settings.json`: تنظیمات کاربر برای زبان و تم را ذخیره می‌کند (به‌صورت خودکار تولید می‌شود).

### مشارکت
مشارکت‌ها استقبال می‌شوند! لطفاً مخزن را فورک کنید، تغییرات خود را اعمال کنید و یک درخواست کشش (pull request) ارسال کنید. اطمینان حاصل کنید که کد شما از سبک کدنویسی پروژه پیروی می‌کند و شامل مستندات مناسب است.

### مجوز
این پروژه تحت مجوز MIT منتشر شده است. برای جزئیات بیشتر، فایل LICENSE را ببینید.

---

## 中文

### 概述
图片库应用程序是一个使用 Python、PyQt6 和 Pillow 构建的桌面应用程序。它允许用户浏览、管理和编辑选定文件夹中的图片。该应用程序支持多种语言、可自定义的主题，并提供图片标签、幻灯片查看以及旋转和裁剪等基本图片编辑功能。

### 功能
- **图片浏览**：从选定文件夹加载并以网格布局显示图片。
- **标签系统**：为图片添加和搜索标签，便于组织。
- **幻灯片模式**：使用导航控件以幻灯片形式查看图片。
- **图片编辑**：向左或向右旋转图片，并使用可自定义参数裁剪图片。
- **多语言支持**：支持英语、波斯语、中文和俄语。
- **主题选择**：提供默认、浅色、深色、红色和蓝色主题，以获得个性化体验。
- **设置持久化**：保存语言和主题偏好以供后续使用。

### 要求
- Python 3.9 或更高版本
- PyQt6
- Pillow (PIL)

### 安装
1. 确保系统中已安装 Python 3.9 或更高版本。
2. 安装所需的依赖项：
   ```bash
   pip install PyQt6 Pillow
   ```
3. 从仓库下载 `photo_gallery.py` 文件。
4. 运行应用程序：
   ```bash
   python photo_gallery.py
   ```

### 使用方法
1. 使用上述命令启动应用程序。
2. 使用“打开文件夹”按钮或菜单选择包含图片的目录。
3. 在标签输入字段中输入标签并按 Enter 键为图片添加标签。
4. 在搜索栏中输入标签以搜索图片。
5. 使用“幻灯片”按钮开始幻灯片播放。
6. 右键单击图片以访问编辑选项（旋转、裁剪）。
7. 通过工具栏下拉菜单更改语言或主题。
8. 通过“关于”菜单查看应用程序信息。

### 项目结构
- `photo_gallery.py`：包含所有逻辑和用户界面实现的主应用程序文件。
- `settings.json`：存储用户的语言和主题偏好（自动生成）。

### 贡献
欢迎贡献！请 fork 仓库，进行更改，并提交拉取请求。确保您的代码遵循项目的编码风格并包含适当的文档。

### 许可证
本项目采用 MIT 许可证发布。有关详细信息，请参阅 LICENSE 文件。