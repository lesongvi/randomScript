/*
 * TẢI TESTCASE VỀ NHỚ XÓA DÒNG NÀY
 * NÉM VÀO TRONG hoangvinh.js
 *
 * Author: Vinh Xua(n-guyen) Hoang
 *
 * Không share đồ của maxmines nhá
 * 4 INTERNAL USE ONLY!
 */

var { By, until, Key } = require('selenium-webdriver');
var { 
    driver,
    base_url,
    testCaseIntroduceStr
} = require('../index.js');
var expect = require('chai').expect;
var { testVars } = require('../helpers/testVariables.js');
var { getDriverConfig } = require('../helpers/driversServices.js');

describe('Test homepage' , async function(){
    this.timeout(999999999999999);
    before(async () => {
        return driver.get(base_url);
    });

    after(async function(){
        driver.quit();
    });

    sleep = (ms) => {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    bypassCaptcha = async () => {
        await driver.findElement(By.xpath("//div[@id=\'captcha\']/maxmines-tempcaptcha")).click();
        await sleep(1000);
        return await driver.executeScript(
            "var play = document.querySelector('maxmines-tempcaptcha').shadowRoot.querySelectorAll('.mma-ttt-td');play[0].click();play[2].click();play[7].click();play[5].click();play[6].click();");
    }
    loginByMaxMinesAccount = async (email, password) => {
        await driver.findElement(By.css(".ml")).click();
        await sleep(2500);
        await driver.findElement(By.id("email")).sendKeys(email);
        await driver.findElement(By.id("password")).sendKeys(password);
        await bypassCaptcha();
        await sleep(2000);
        await driver.findElement(By.xpath("//button[@type='submit']")).click();
        await sleep(2000);
        return new Promise((resolve, reject) => {
            driver.findElements(By.css(".alert-error")).then(el => {
                if (el.length !== 0)
                    return driver.findElement(By.css(".alert-error")).getText().then(text => reject(text));
                else return resolve();
            })
        });
    }
    registerByMaxMinesAccount = async (name, email, password) => {
        await driver.findElement(By.id("name")).sendKeys(name);
        await driver.findElement(By.id("email")).sendKeys(email);
        await driver.findElement(By.id("password")).sendKeys(password);
        await driver.findElement(By.id("password_confirmation")).sendKeys(password);
        await bypassCaptcha();
        await sleep(500);
        // await driver.findElement(By.xpath("//label")).click();
        await driver.executeScript("document.querySelectorAll('div.checkbox')[0].click()");
        await sleep(1500);
        await driver.findElement(By.xpath("//button[@type='submit']")).click();
        await sleep(2000);
        return new Promise((resolve, reject) => {
            driver.findElements(By.css(".alert-error")).then(el => {
                if (el.length !== 0)
                    return driver.findElement(By.css(".alert-error")).getText().then(text => reject(text));
                else return resolve();
            })
        });
    }
    rfun = (mn, mx) => {
        return Math.floor(Math.random() * (mx - mn) + mn);
    }
    selectByAHref = (pathname) => "//a[contains(@href, '" + pathname + "')]";
    ranChars = (length) => {
        for (var result = "", characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", charactersLength = characters.length, i = 0; i < length; i++) 
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        return result;
    }

    afterEach(function () {
        driver.manage().deleteAllCookies();
        driver.close();
        driver = getDriverConfig('chrome');
        return driver.get(base_url);
    });

    beforeEach(async function () {
        await sleep(2000);
        var tcObj = testCaseIntroduceStr[this.currentTest.title];
        var form = `Tên testcase: ${tcObj.name}\n\nMô tả testcase:\n${tcObj.desc}\n\nĐơn giản/Nâng cao: ${tcObj.type == "basic" ? "Đơn giản" : "Nâng cao"}\n\nViết bởi: ${tcObj.author}`
        await driver.executeScript("alert(`" + form + "`)");
        var alert = driver.switchTo().alert();
        while (alert) {
            await sleep(1000);
            alert = await driver.switchTo().alert().getText().then(text => {
                return text
            }).catch(err => {
                return null
            })
        }
        await driver.wait(function () {
            return until.elementIsVisible(By.id(":xksiwm_"));
        }, 50000);
        await driver.wait(function () {
            return until.elementIsVisible(By.id("appMClose"));
        }, 50000);
        await sleep(3000);
        await driver.findElement(By.id("appMClose")).click();
    });

    /*
     * 1. Test case kiểm tra ngôn ngữ
     * 
     * Mô tả testcase: 
     * Truy cập trang chủ MaxMines, kiểm tra nội dung của class 'get-started'.
     * Chuyển ngôn ngữ, kiểm tra nội dung 'get-started'. Chuyển về lại ngôn ngữ ban đầu, kiểm
     * tra nội dung 'get-started'
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testChangeLanguage', async function () {
        await driver.findElement(By.css(".medium.get-started")).getText().then(async text => {
            expect(text).equal("TÍCH HỢP MAXMINES VÀO ỨNG DỤNG CỦA BẠN");
            sleep(1000);
            await driver.findElement(By.css(".vSelect__single-value")).click();
            await driver.findElement(By.id("react-select-2-option-0")).click();
            await driver.findElement(By.css(".medium.get-started")).getText().then(async text => {
                expect(text).equal("INTEGRATE MAXMINES ON YOUR APPLICATION");
                sleep(1000);
                await driver.findElement(By.css(".vSelect__single-value")).click();
                await driver.findElement(By.id("react-select-2-option-1")).click();
                await driver.findElement(By.css(".medium.get-started")).getText().then(async text => {
                    sleep(1000);
                    expect(text).equal("TÍCH HỢP MAXMINES VÀO ỨNG DỤNG CỦA BẠN");
                });
            });
        });
    });

    /*
     * 2. Test case đăng nhập thất bại
     * 
     * Mô tả testcase: 
     * Truy cập trang chủ MaxMines, truy cập vào trang đăng nhập, nhập
     * email không hợp lệ để kiểm tra lỗi trả về
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testInvalidLogin', async () => {
        await driver.findElement(By.xpath(testVars.homePageLoginBtn)).click();
        await sleep(3000);
        await loginByMaxMinesAccount("test@test.com", "123456")
        .then(async () => {
            expect(true).to.equal(false);
        }).catch(err => {
            expect(err).to.equal("Sai thông tin tài khoản");
        });
    });

    /*
     * 3. Test case đăng ký thất bại (email tồn tại)
     * 
     * Mô tả testcase: 
     * Truy cập trang chủ MaxMines, truy cập vào trang đăng ký, nhập
     * email tester@roleplay.vn (email đã đăng ký) để kiểm tra lỗi trả 
     * về.
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testInvalidEmailRegister', async () => {
        await driver.findElement(By.xpath(testVars.homePageRegisterBtn)).click();
        await sleep(3000);
        await registerByMaxMinesAccount("tester9999", "tester@roleplay.vn", "Abcdef123!@#")
        .then(async () => {
            expect(true).to.equal(false);
        }).catch(err => {
            expect(err).to.equal("The email has already been taken.");
        });
    });

    /*
     * 4. Test case đăng ký thất bại (tên đăng nhập tồn tại)
     * 
     * Mô tả testcase: 
     * Truy cập trang chủ MaxMines, truy cập vào trang đăng ký, nhập
     * tên tài khoản tester (tên tài khoản đã đăng ký) để kiểm tra 
     * lỗi trả về.
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testInvalidUsernameRegister', async () => {
        await driver.findElement(By.xpath(testVars.homePageRegisterBtn)).click();
        await sleep(3000);
        await registerByMaxMinesAccount("tester", "testerz223@roleplay.vn", "Abcdef123!@#")
        .then(async () => {
            expect(true).to.equal(false);
        }).catch(err => {
            expect(err).to.equal("The name has already been taken.");
        });
    });

    /*
     * 5. Test case đăng ký thất bại (cả tên đăng nhập và email tồn tại)
     * 
     * Mô tả testcase: 
     * Truy cập trang chủ MaxMines, truy cập vào trang đăng ký, nhập
     * tên tài khoản tester (tên tài khoản đã đăng ký) và địa chỉ email
     * là tester@roleplay.vn để kiểm tra lỗi trả về.
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testInvalidUsernameAndEmailRegister', async () => {
        await driver.findElement(By.xpath(testVars.homePageRegisterBtn)).click();
        await sleep(3000);
        await registerByMaxMinesAccount("tester", "tester@roleplay.vn", "Abcdef123!@#")
        .then(async () => {
            expect(true).to.equal(false);
        }).catch(err => {
            expect(err).to.equal("The name has already been taken.The email has already been taken.");
        });
    });

    /*
     * 6. Test case tìm theo khối băm trong explorer
     * 
     * Mô tả testcase: 
     * Truy cập trang mạng lưới MaxMines, lấy ngẫu nhiên 1 mã băm trong bảng
     * Nhập vào tìm kiếm, kiểm tra băm trả về có đúng không
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testExlorer1', async () => {
        await driver.findElement(By.xpath("//a[contains(@href, '/explorer')]")).click();
        await sleep(10000);
        await driver.findElements(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div[2]/div/table/tbody/tr"))
        .then(async elm => {
            var rnd = Math.floor(Math.random() * (elm.length - 1) + 1);
            await driver.findElement(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div[2]/div/table/tbody/tr[${rnd}]/td[2]/a`))
            .getText().then(async t1 => {
                await driver.findElement(By.name("searchString")).sendKeys(t1);
                await sleep(500);
                await driver.findElement(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div/div[2]/i")).click();
                await sleep(5000);
                await driver.findElement(By.xpath("//div[@id='content']/div[3]/div[2]/div/div/div/div[2]/div/div/p[2]"))
                .getText().then(async t2 => {
                    expect(t1).to.equal(t2);
                });
            })
        });
    });

    /*
     * 7. Test case tìm theo chiều cao trong explorer
     * 
     * Mô tả testcase: 
     * Truy cập trang mạng lưới MaxMines, lấy ngẫu nhiên 1 chiều cao trong bảng
     * Nhập vào tìm kiếm, kiểm tra chiều cao trả về có đúng không
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testExlorer2', async () => {
        await driver.findElement(By.xpath("//a[contains(@href, '/explorer')]")).click();
        await sleep(10000);
        await driver.findElements(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div[2]/div/table/tbody/tr"))
        .then(async elm => {
            var rnd = Math.floor(Math.random() * (elm.length - 1) + 1);
            await driver.findElement(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div[2]/div/table/tbody/tr[${rnd}]/td[1]/a`))
            .getText().then(async t1 => {
                await driver.findElement(By.name("searchString")).sendKeys(t1);
                await sleep(500);
                await driver.findElement(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div/div[2]/div/div/div[2]/i")).click();
                await sleep(5000);
                await driver.findElement(By.xpath("//div[@id='content']/div[3]/div[2]/div/div/div/div[2]/div/div[2]/p[2]"))
                .getText().then(async t2 => {
                    expect(t1).to.equal(t2);
                });
            })
        });
    });

    /*
     * 8. Test case lọc blog theo thể loại
     * 
     * Mô tả testcase: 
     * Truy cập trang blog, chọn ngẫu nhiên 1 thẻ blog
     * Kiểm tra xem blog trả về có chứa thẻ không
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testBlogTag', async () => {
        await driver.navigate().to("https://maxmines.com/blog");
        await sleep(5000);
        await driver.findElements(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div/div/div[2]/a"))
        .then(async elm => {
            var rnd = Math.floor(Math.random() * (elm.length - 1) + 1);
            await driver.findElement(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div/div/div[2]/a[${rnd}]`)).click();
            await sleep(2500);
            await driver.findElement(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div/div/div[2]/a[${rnd}]`))
            .getText().then(async tag => {
                await sleep(2000);
                await driver.findElements(By.xpath("//div[@id=':xksiwm_']/div[4]/div/div[2]/div[2]/div"))
                .then(async elm => {
                    for (var i = 1;i <= elm.length;i++) {
                        await driver.findElements(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div[2]/div[2]/div[${i}]/div/div/a`))
                        .then(async melm => {
                            var tagLogg = [];
                            for (var idx = 1;idx <= melm.length-1;idx++) {
                                await driver.findElement(By.xpath(`//div[@id=':xksiwm_']/div[4]/div/div[2]/div[2]/div[${i}]/div/div/a[${idx}]`))
                                .getText().then(async text => {
                                    tagLogg.push(text);
                                    if (idx == melm.length - 1) {
                                        await expect(tagLogg).to.include(tag);
                                    }
                                });
                            }
                        })
                    }
                });
            })
        });
    });

    /*
     * 9. Test case kiểm tra nút hiện / ẩn mật khẩu
     * 
     * Mô tả testcase: 
     * Truy cập trang đăng nhập, nhập mật khẩu bất kỳ
     * Nhấp vào biểu tượng hình con mắt để xem mật
     * khẩu có bị ẩn hay không
     * 
     * Kiểu testcase: Đơn giản
     * 
     * Author: Nguyễn Hoàng Vinh
     */
    it('testHidePassword', async () => {
        await driver.navigate().to("https://maxmines.com/my/register");
        await sleep(5000);
        await driver.findElement(By.id("password")).getAttribute("type")
        .then(async t1 => {
            expect(t1).to.equal("password");
            await driver.findElement(By.id("password_confirmation")).getAttribute("type")
            .then(async t2 => {
                expect(t2).to.equal("password");
                await driver.findElement(By.xpath("//div[@id='content']/div/div[2]/div/div/form/div[3]/div/div[2]/i")).click();
                await sleep(1000);
                await driver.findElement(By.id("password")).getAttribute("type")
                .then(async t1 => {
                    expect(t1).to.equal("text");
                    await driver.findElement(By.xpath("//div[@id='content']/div/div[2]/div/div/form/div[5]/div/div[2]/i")).click();
                    await sleep(1000);
                    await driver.findElement(By.id("password_confirmation")).getAttribute("type")
                    .then(async t2 => {
                        expect(t2).to.equal("text");
                        await driver.findElement(By.xpath("//div[@id='content']/div/div[2]/div/div/form/div[3]/div/div[2]/i")).click();
                        await sleep(1000);
                        await driver.findElement(By.id("password")).getAttribute("type")
                        .then(async t1 => {
                            expect(t1).to.equal("password");
                            await driver.findElement(By.xpath("//div[@id='content']/div/div[2]/div/div/form/div[5]/div/div[2]/i")).click();
                            await sleep(1000);
                            await driver.findElement(By.id("password_confirmation")).getAttribute("type")
                            .then(async t2 => {
                                expect(t2).to.equal("password");
                            });
                        });
                    });
                });
            });
        });
    });
});
