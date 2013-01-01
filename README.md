This is Selenium project
to monitor ShopYourWay frame.

1. disable IPV6
2. easy_install virtualenv
3. virtualenv selenv
4. cd selenv
5. bin/pip install selenium
6. wget http://selenium.googlecode.com/files/selenium-server-standalone-2.28.0.jar
7. wget http://releases.mozilla.org/pub/mozilla.org/firefox/releases/17.0.1/linux-i686/en-US/firefox-17.0.1.tar.bz2
8. tar -xvf firefox-17.0.1.tar.bz2
9. ln -s /opt/selenv/firefox/firefox /usr/bin/firefox
10. Install headless java
sudo apt-get install openjdk-6-jre-headless
11. Fonts
sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
12. Headless X11 magic is here
sudo apt-get install xvfb
13. We still demand X11 core
sudo apt-get install xserver-xorg-core

