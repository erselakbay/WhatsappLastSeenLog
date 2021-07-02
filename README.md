# Whatsapp Last Seen Log

-ENG- 

WhatsappLastSeenLog is a project built with python that uses selenium to log user's last seen status to a .txt file.

-TR-
 
WhatsAppLastSeenLog, kullanıcının son görülme durumunu bir .txt dosyasına kaydetmek için selenyum kullanarak python ile oluşturulmuş bir projedir.

## Use With .bat
python online.py "https://web.whatsapp.com/" "Name"
pause

![img](images/example1.png)

-ENG- 

-Change the contents of the .bat file in the folder as in the example image without having to write commands for python with cmd.
(Only one user's name should be written. Multiple users are not supported.)

-save the changed file

-run the .bat file by double clicking on it

Thats All. The program will automatically create the user's history and log files for you and start writing the content.

Note: All installations related to python, selenium and pytesseract must be completed for the program to work.



-TR-  

-Cmd ile python için komut yazmak zorunda kalmadan, örnek görüntüdeki gibi klasördeki .bat dosyasının içeriğini değiştirin. 
(Yalnızca tek bir kullanıcının ismi yazılmalıdır. Birden fazla kullanıcı desteklenmemektedir.)

-Değiştirilen dosyayı kaydedin.

-.bat dosyasını çift tıklayarak çalıştırın

Hepsi bu kadar. Program sizin için kullanıcının geçmiş ve log dosyalarını otomatik olarak oluşturacak ve içeriğini yazmaya başlayacaktır.

Not: Programın çalışması için python, selenium ve pytesseract ile ilgili tüm kurulumların tamamlanması gerekir.

## Details About .txt Files

**Name_History.txt:**

![img](images/example2.png)

**Name_Log:**

![img](images/example3.png)