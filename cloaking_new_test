
package maby_now;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class Segmentation_Full_test {
	public static void telegram_alert(String str) throws InterruptedException {
		String telegaAPIurl1 = "https://api.telegram.org/bot5520811460:AAEiMSM8ZozY6EHVEEeTGeX3oyGxdzHRVC0/sendMessage?chat_id=@CloackerNotify&text=%7B";
		String telegaAPIurl2 =  "%7D";
		Object alert =buid_driver_fun();
		((WebDriver) alert).get(telegaAPIurl1 + str + telegaAPIurl2);
		((WebDriver) alert).close();
	}
	public static Object buid_driver_fun() throws InterruptedException {
	   	System.setProperty("webdriver.chrome.driver","C:\\seleniumStuff\\Lamda_python_selenium//chromedriver.exe");
    	WebDriver driver = new ChromeDriver();
    	return (driver);
	}
	public static void main(String[] args) throws InterruptedException {
		
		//domain URL's app = 5452-test-regular-amazon || 8000 = 8075-Andrei-don't-touch
		String wehave = "https://www.wehavethebestgames.info/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5&id_app=hyxtuthjeiged&gl_app=uttrbxmfpdtvexw&admob_app=mdegcdkipwojrqjaxcc";
		String registration = "https://www.registrationneedclick.com/apps-maker.php?website=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String funwebsitegame = "https://www.funwebsitegames.info/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String smart = "https://www.smartappsmobi.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String globalservicesfree = "https://globalservicesfree.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		
		//cloaking URL's: presstoplay * all cloakers
		String press2_index_php = "https://presstoplayfun.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String press2_Ana_con_php = "https://presstoplayfun.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String press2_Ana_con_token = "https://presstoplayfun.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		String press2_clocker_php = "https://presstoplayfun.com/stats/lambda/cloaker.php?app=5452-pressToplayAnaConToken&token=THETOKEN";
		String preesstoplay_V2 = "https://presstoplayfun.com/cloaker2.0/cloaker_v2.php?app=5452-test-token-cloaker_V2-press2&ut=123";	
		
		//http://webmilleniumtopmarket.com/stopeatvegan * index| ana_con| ana_con_token|cloaker.php
		String Webmillenium_index_php = "https://stopeatvegan.com/index.php?dapn=5452-test-regular-amazon";
		String Webmillenium_Ana_con_php = "https://stopeatvegan.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String Webmillenium_Ana_con_token = "https://stopeatvegan.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		// https://webmilleniumtopmarket.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=
		// https://webmilleniumtopmarket.com/index.php?dapn=5452-test-regular-amazon
		// https://webmilleniumtopmarket.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u
		// without token -> regular cloaker :
		// https://webmilleniumtopmarket.com/stats/lambda/cloaker.php?app=5452-test-regular-amazon
		// with token - cloker php case :
		String Webmillenium_clocker_php = "https://webmilleniumtopmarket.com/stats/lambda/cloaker.php?app=5452-POP-UP-TEST&token=token1";
		//String Webmillenium_clocker_php = "https://stopeatvegan.com/stats/lambda/cloaker.php?app=5452-test-regular-amazon";
		
		//globalwarmingindicator * index| ana_con| ana_con_token
		String globalwarming_index_php = "https://globalwarmingindicator.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String globalwarming_Ana_con_php = "https://globalwarmingindicator.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String globalwarming_Ana_con_token_php = "https://globalwarmingindicator.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		//links located in array's
		String[] clocking_Url= {press2_index_php,press2_Ana_con_php,press2_Ana_con_token,Webmillenium_index_php,Webmillenium_Ana_con_php,Webmillenium_Ana_con_token,globalwarming_index_php,globalwarming_Ana_con_php,globalwarming_Ana_con_token_php};
		String[] cloaking_url_with_body_response = {press2_clocker_php,preesstoplay_V2,Webmillenium_clocker_php};
		String[] production_domains = {wehave, registration, funwebsitegame, smart, globalservicesfree};
		
		
		String[] responseArr= {"","","","","","","","",""};
		
		//Domain Url's: wehave + fun + global + registration + smart - QA Enviroment
		// application : QA-Environment : { 5452-test-regular-amazon || 8075-Andrei-new-check-for-something }
		String wehave_QA = "https://www.wehavethebestgamesqa.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5&id_app=hyxtuthjeiged&gl_app=uttrbxmfpdtvexw&admob_app=mdegcdkipwojrqjaxcc";
		String fun_QA = "https://www.sw.funwebsitegamesqa.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String global_QA = "https://globalservicesfreeqa.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String registration_QA = "https://www.sw.registrationneedclickqa.com/apps-maker.php?website=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		String smart_QA = "https://www.sw.smartappsmobiqa.com/?cd_app=03x2t2w21406b4y516s2x5c4k5s4p574y514h5e4e5u4k4r5";
		
		
		// Cloaking URL's -> QA Enviromen :
		String press2_index_php_QA = "https://sw.presstoplayfunqa.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";//click
		String press2_Ana_con_php_QA = "https://sw.presstoplayfunqa.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String press2_Ana_con_token_QA = "https://sw.presstoplayfunqa.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		String press2_clocker_php_QA = "https://sw.presstoplayfunqa.com/stats/lambda/cloaker.php?app=5452-pressToplayAnaConToken&token=THETOKEN";
		String preesstoplay_V2_QA = "https://sw.presstoplayfunqa.com/cloaker2.0/cloaker_v2.php?app=5452-test-token-cloaker_V2-press2&ut=ANDREI";
		String Webmillenium_index_php_QA = "http://sw.webmilleniumtopmarketqa.com/index.php?dapn=5452-test-regular-amazon ";
		String Webmillenium_Ana_con_php_QA = "http://sw.webmilleniumtopmarketqa.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String Webmillenium_Ana_con_token_QA = "http://sw.webmilleniumtopmarketqa.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		String Webmillenium_clocker_php_QA = "http://sw.webmilleniumtopmarketqa.com/stats/lambda/cloaker.php?app=5452-test-regular-amazon";
		String globalwarming_index_php_QA = "https://pk.globalwarmingindicatorqa.com/index.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String globalwarming_Ana_con_php_QA = "https://pk.globalwarmingindicatorqa.com/ana_con.php?apn=NTQ1Mi10ZXN0LXJlZ3VsYXItYW1hem9u";
		String globalwarming_Ana_con_token_php_QA = "https://pk.globalwarmingindicatorqa.com/ana_con_token.php?apn=NTQ1Mi1wcmVzc1RvcGxheUFuYUNvblRva2Vu&ut=VEhFVE9LRU4=";
		
		String[] qa_domains = {wehave_QA,fun_QA, global_QA, registration_QA, smart_QA};
		String[] qa_clocking_Url = {press2_index_php_QA, press2_Ana_con_php_QA, press2_Ana_con_token_QA,  Webmillenium_index_php_QA, Webmillenium_Ana_con_php_QA, Webmillenium_Ana_con_token_QA, globalwarming_index_php_QA, globalwarming_Ana_con_php_QA, globalwarming_Ana_con_token_php_QA};	
		String[] qa_cloaking_url_with_body_response = {press2_clocker_php_QA, preesstoplay_V2_QA, Webmillenium_clocker_php_QA}; 
		
//====================================================================================================================================================================================================================================================================================================================================================================		
		//test code:
		
		String isBLockedIP  = "&ip=104.23.0.0";
		System.setProperty("webdriver.chrome.driver","C:\\seleniumStuff\\Lamda_python_selenium//chromedriver.exe");
		
		WebDriver driver = new ChromeDriver();
		
		/*driver.get("http://mobileservicesnow.in");
		driver.manage().window().maximize();
		driver.get("http://mobileservicesnow.in/odds_link_maker.php");
		driver.findElement(By.xpath("//*[@id=\"login\"]//div")).sendKeys("andrei");
		driver.findElement(By.xpath("//*[@id=\"pass\"]")).sendKeys("jvQ*U0y0)Flh0n3H");
		driver.findElement(By.xpath("//*[@id=\"main\"]/div[1]/form/input[3]")).click();
		driver.get("http://mobileservicesnow.in/odds_link_maker.php");
		driver.findElement(By.xpath("/html/body/form/input[1]")).sendKeys("8075-Andrei");
		driver.findElement(By.xpath("/html/body/form/input[2]")).sendKeys("5452-pressToplayAnaConToken");
		driver.findElement(By.xpath("/html/body/form/input[3]")).sendKeys("5452");
		driver.findElement(By.xpath("/html/body/form/input[4]")).click();
		String oddMagicURL = driver.findElement(By.xpath("/html/body/form/input[5]")).getAttribute("value");
		Thread.sleep(5000);
		
		
		
		//local-test  - START - //
		driver.get("http://myservicessapps.com/ipp.php");
		driver.get(oddMagicURL);
		telegram_alert(oddMagicURL);
		*/
		//run the system domains : 
		for (int i = 0; i < production_domains.length; i++) {
			driver.get(production_domains[i]);
			telegram_alert(production_domains[i]);
			Thread.sleep(3000);
		}
		for (int i = 0; i < clocking_Url.length; i++) {
			driver.get(clocking_Url[i]);
			telegram_alert(clocking_Url[i]);
			Thread.sleep(3000);
			responseArr[i]= driver.findElement(By.xpath("/html/body")).getText();
		}//run the responses
		for (int i = 0; i < responseArr.length; i++) {
			driver.get(responseArr[i]);
			telegram_alert(responseArr[i]);
			Thread.sleep(6000);
			System.out.println(responseArr[i]);
		}
		driver.close();
		//end of proxy test -------------------------------------------------------/////
		
		WebDriver driver_system = new ChromeDriver();
		driver_system.get("http://mobileservicesnow.in");
		driver_system.manage().window().maximize();
		driver_system.findElement(By.xpath("//*[@id=\"login\"]")).sendKeys("andrei");
		driver_system.findElement(By.xpath("//*[@id=\"pass\"]")).sendKeys("jvQ*U0y0)Flh0n3H");
		driver_system.findElement(By.xpath("//*[@id=\"main\"]/div[1]/form/input[3]")).click();
		
		driver_system.get("http://mobileservicesnow.in/checking/last-100-search-today.php");
		driver_system.findElement(By.xpath("/html/body/form/input[8]")).sendKeys("5452");
		driver_system.findElement(By.xpath("/html/body/form/input[10]")).click();
	} // u should see 17 clicks with your slug in System 
	
	
}
