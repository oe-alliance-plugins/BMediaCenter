from setuptools import setup
import setup_translate

pkg = 'Extensions.BMediaCenter'
setup(name='enigma2-plugin-extensions-bmediacenter',
       version='3.0',
       description='Make your Receiver to a MediaCenter',
       package_dir={pkg: 'BMediaCenter'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'keymap.xml', 'plugin.png', 'setup.xml', 'icons/*.png', 'icons/screenadjust.mvi', 'radio/*.pls', 'radio/*.m3u', 'saver/*.jpg', 'skins/defaultHD/skin.xml', 'skins/defaultHD/images/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
