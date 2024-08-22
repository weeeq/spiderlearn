手机号api接口测试

介绍
这个项目是一个 Python 脚本，用于自动化处理手机号验证码获取任务。脚本利用 Selenium WebDriver 控制 Microsoft Edge 浏览器，通过输入手机号并点击“获取验证码”按钮来自动化完成任务。该脚本支持多线程并行处理，能够同时在多个浏览器窗口中运行。

功能
自动化登录到指定网站
遍历手机号列表，自动输入手机号并点击“获取验证码”按钮
检查按钮状态，根据需要进行点击操作
等待验证码重新发送的提示并刷新页面
支持多线程并行处理，能够在多个浏览器窗口中运行

环境要求
Python 3.x
Selenium WebDriver
Microsoft Edge 浏览器




Mobile Number API Testing

Introduction
This project is a Python script designed for automating the process of retrieving verification codes for mobile numbers. The script uses Selenium WebDriver to control the Microsoft Edge browser, automating the task of entering mobile numbers and clicking the "Get Verification Code" button. The script supports multi-threaded parallel processing, allowing it to run in multiple browser windows simultaneously.

Features
Automates login to the specified website
Iterates through a list of mobile numbers, inputs the numbers, and clicks the "Get Verification Code" button
Checks the button status and performs clicking operations as needed
Waits for the "Resend" prompt and refreshes the page
Supports multi-threaded parallel processing across multiple browser windows

Requirements
Python 3.x
Selenium WebDriver
Microsoft Edge browser


