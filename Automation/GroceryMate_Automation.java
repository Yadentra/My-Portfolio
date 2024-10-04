import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
public class GroceryMateAutomation {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver"); // Replace with your chromedriver path
        WebDriver driver = new ChromeDriver();
        
        // Open Grocery Mate webshop
        driver.get("https://grocerymate.com");
        
        // Test the product search functionality
        driver.findElement(By.name("search")).sendKeys("apple");
        driver.findElement(By.id("search-button")).click();
        
        // Verify search results
        String result = driver.findElement(By.id("search-results")).getText();
        System.out.println("Search Results: " + result);
        
        // Close the browser
        driver.quit();
    }
}
