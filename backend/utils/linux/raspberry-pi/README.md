## Instalaciones
### Testing con Python/Selenium
```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.16.0/geckodriver-v0.16.0-arm7hf.tar.gz
tar -xvzf geckodriver-v0.16.0-arm7hf.tar.gz
sudo mv geckodriver /usr/local/bin/geckodriver
sudo apt-get install iceweasel xvfb
pip3 install pyvirtualdisplay selenium==3.3.2
```

```python
from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = webdriver.firefox.firefox_binary.FirefoxBinary(self._firefox_binary)
browser = webdriver.Firefox(firefox_binary=binary)

# Ejecutamos los tests

browser.quit()
display.stop()
```

_______________________________________________
