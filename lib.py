from selenium import webdriver

def get_firefox():
	# workaround http://code.google.com/p/selenium/issues/detail?id=2863
	fp = webdriver.FirefoxProfile()
	fp.set_preference("capability.policy.default.HTMLDocument.readyState","allAccess")
	fp.set_preference("capability.policy.default.HTMLDocument.compatMode","allAccess")
	fp.set_preference("capability.policy.default.Document.compatMode","allAccess")
	fp.set_preference("capability.policy.default.Location.href","allAccess")
	fp.set_preference("capability.policy.default.Window.pageXOffset","allAccess")
	fp.set_preference("capability.policy.default.Window.pageYOffset","allAccess")
	fp.set_preference("capability.policy.default.Window.frameElement","allAccess")
	fp.set_preference("capability.policy.default.Window.frameElement.get","allAccess")
	fp.set_preference("capability.policy.default.Window.QueryInterface","allAccess")
	fp.set_preference("capability.policy.default.Window.mozInnerScreenY","allAccess")
	fp.set_preference("capability.policy.default.Window.mozInnerScreenX","allAccess")
	return webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX, browser_profile=fp)
#	return webdriver.Firefox(fp)
