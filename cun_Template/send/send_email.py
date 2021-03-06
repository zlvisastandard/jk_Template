# coding:utf-8   #强制使用utf-8编码格式
import smtplib  #加载smtplib模块from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.utils import formataddr
class SendEmail(object):
    def mail(self,user_list,sub,content):
        my_sender='' #发件人邮箱账号，为了后面易于维护，所以写成了变量

        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["发件人邮箱昵称",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人邮箱昵称",user_list])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']=sub #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[user_list],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思


    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)

        user_list = ''
        sub = "接口自动化测试报告"
        content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
        self.mail(user_list,sub,content)
if __name__ == '__main__':
    a = [1,2,3,4]
    b = [2,3,4,5,6,7]
    ret = SendEmail()
    data = ret.send_main(a,b)

