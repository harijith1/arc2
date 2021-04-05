x=1
y=0
o=0

while o==0:
    o +=1
    
    #TO AUTHENTICATE
    print ("Hello, welcome to the ARC billing interface")
    k = input("Please enter your password : ")
    m = int(k)
    if m==1996:
        print ("ACCESS GRANTED")
        #FOR UPDATING MASTER BILL
        d=open('C:\\Users\Padmapriya\Desktop\Total.txt','at')
        d.write ('\n')
        d.close()
        #FOR UPDATING SINGLE TEXT BILL
        q=open('C:\\Users\Padmapriya\Desktop\Bill.txt','wt')
        q.write ('\n'+'ARC INDUSTRIES')
        q.write ('\n'+'Invoice'+'\n'+'\n')
        q.write ('\n'+'---------------------------------------------------------------'+'\n')
        q.close()
        #FOR UPDATING HTML BILL
        doc=open('C:\\Users\Padmapriya\Desktop\Bill.html','wt')
        doc.write ('\n'+'<!DOCTYPE html><html><center><h1>ARC INDUSTRIES</h1></center>')
        doc.write ('\n'+'<center><h2>Invoice</h2></center>'+'\n'+'<br><hr>')
        doc.write ('\n'+'<center><table>'+'\n'+'<colgroup>'+'\n'+'<col span="2">'+'\n'+'</colgroup>'+'\n'+'<tr><th>ITEM CODE</th><th>PRICE</th></tr>')
        doc.close()

        a = ("Press 'enter' after entering the values")
        while x<500:
            print (a)
            b = input("Item code:")
            f=int(b)
            if f>0:
                c = input("Price:")
                print ('Item code: '+b)
                print (c+' Rs')
                p=int(c)
                #FOR UPDATING MASTER BILL
                e=open('C:\\Users\Padmapriya\Desktop\Total.txt','at')
                e.write ('Item code: '+b)
                e.write ('\n'+c+' Rs'+'\n'+'\n')
                e.close()
                #FOR UPDATING SINGLE TEXT BILL
                r=open('C:\\Users\Padmapriya\Desktop\Bill.txt','at')
                r.write ('Item code: '+b)
                r.write ('\n'+c+' Rs'+'\n'+'\n')
                r.close()
                #FOR UPDATING HTML BILL
                h=open('C:\\Users\Padmapriya\Desktop\Bill.html','at')
                h.write ('\n'+'<tr>'+'\n'+'<td>'+b+'</td>')
                h.write ('\n'+'<td>'+c+' Rs</td>'+'\n'+'</tr>')
                h.close()
                x += 1
                y += p
                u=str(y)
                print ("Total:"+u+" Rs")
            elif f==0:
                x=501
                
                # Python code to illustrate Sending mail with attachments 
                # from your Gmail account 

                # libraries to be imported 
                import smtplib 
                from email.mime.multipart import MIMEMultipart 
                from email.mime.text import MIMEText 
                from email.mime.base import MIMEBase 
                from email import encoders 

                fromaddr = "arcgroupinterest@gmail.com"
                toaddr = input("Please enter client's e-mail ID : ")
                print ("PROCESSING...PLEASE WAIT...")
                
                #FOR UPDATING HTML BILL
                v=open('C:\\Users\Padmapriya\Desktop\Bill.html','at')
                v.write ('\n'+'<tr><td id="total"><b>YOU PAY</b></td><td id="total"><b> '+ u +' Rs</b></td></table></center>')
                v.write ('\n'+'<center><h2>Bill sent to : '+toaddr+' </h2></center>')
                v.write ('\n'+'<center><h2>Thank you for shopping with us</h2></center>'+'<center><h2 id="green">GO GREEN!</h2></center>'+'\n'+'<br><hr><style>#green{color:green;}#total{background-color:yellow;}th,td{width:200px;margin:5px;text-align:center;}table,th,td{border:1px solid black;}th{background-color:#d8d8d8;}</style></body></html>')
                v.close()

                # instance of MIMEMultipart 
                msg = MIMEMultipart() 

                # storing the senders email address 
                msg['From'] = fromaddr 

                # storing the receivers email address 
                msg['To'] = toaddr 

                # storing the subject 
                msg['Subject'] = "ARC INVOICE | Paper-free initiative by ARC"

                # string to store the body of the mail 
                body = "KINDLY FIND ATTACHED HEREWITH, THE INVOICE FOR YOUR PURCHASE TODAY. THANK YOU FOR SHOPPING WITH US AND ALSO FOR SUPPORTING OUR PAPER-FREE INITIATIVE. GO GREEN!"

                # attach the body with the msg instance 
                msg.attach(MIMEText(body, 'plain')) 

                # open the file to be sent 
                filename = "Bill.html"
                attachment = open("C:\\Users\Padmapriya\Desktop\Bill.html", "rb") 

                # instance of MIMEBase and named as p 
                p = MIMEBase('application', 'octet-stream') 

                # To change the payload into encoded form 
                p.set_payload((attachment).read()) 

                # encode into base64 
                encoders.encode_base64(p) 

                p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

                # attach the instance 'p' to instance 'msg' 
                msg.attach(p) 

                # creates SMTP session 
                s = smtplib.SMTP('smtp.gmail.com', 587) 

                # start TLS for security 
                s.starttls() 

                # Authentication 
                s.login(fromaddr, "arcincgroup") 

                # Converts the Multipart msg into a string 
                text = msg.as_string() 

                # sending the mail 
                s.sendmail(fromaddr, toaddr, text) 

                # terminating the session 
                s.quit()

                #FOR UPDATING MASTER BILL
                e=open('C:\\Users\Padmapriya\Desktop\Total.txt','at')
                e.write ('Total = '+ u +' Rs')
                e.write ('\n'+'Bill sent to : '+toaddr)
                e.write ('\n'+'---------------------------------------------------------------')
                e.close()
                #FOR UPDATING SINGLE TEXT BILL
                s=open('C:\\Users\Padmapriya\Desktop\Bill.txt','at')
                s.write ('Total = '+ u +' Rs')
                s.write ('\n'+'Bill sent to : '+toaddr)
                s.write ('\n'+'Thank you for shopping with us'+'\n'+'---------------------------------------------------------------')
                s.close()
                
                

                print ("Bill paid and closed")
                print("--------------------------------------------------")
    elif m !=1996:
        o=0
        print("ACCESS DENIED")

            

