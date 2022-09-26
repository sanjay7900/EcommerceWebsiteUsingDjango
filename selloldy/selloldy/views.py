from email.mime import message
import imp
from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render,redirect
from matplotlib import image
import razorpay
from django.http import JsonResponse
import datetime
from httpx import request
#from numpy import product
from user.models import Product_info, Userlogin,add_to_cart,chat_contact,chat_messages,paymentHistory
from myclasses.login_auth import logincheck,sign_up

username=''
password=''
identity=-1
personal_information=[]

def about(res):
    # data=Product_info.objects.all()
    # for i in data:
    #     print("sanjay",i.product_name)
    # con={'data':data,'user':''}
    if 'userid' not in res.session:
        return render(res,"login.html")
    else:
        return redirect("http://127.0.0.1:8000/indexpage")
def hii(res):
    # firs=res.POST['email']
    # pas=res.POST['pas']   
    # return HttpResponse(firs+pas) 
    if 'userid' in res.session:
        data=Product_info.objects.all()
    
        for i in data:
            #request.session['user']=i.product_name
            print("sanjay",)
        countcart=add_to_cart.objects.filter(who_is_to_add_id=res.session.get('userid')) 
       
        con={'data':data,'cuntnum':len(countcart)}
        return render(res,"index.html",con)
    else:
        return redirect('http://127.0.0.1:8000')




def pay(res):
    send_provider_info=''
    send_product_information=''
    provider_id=''
    
    if 'userid' in res.session:
        if 'product_id' in res.GET:
            contactuser=Userlogin.objects.filter(id=res.session.get('userid')).values('contact')[0]
            personal_information=[res.session.get('username'),res.session.get('userid'),res.session.get('useremail'),contactuser.get('contact')]
            product_information=Product_info.objects.filter(id=int(res.GET['product_id']))
            for i in product_information:
                provider_info=Userlogin.objects.filter(id=i.provider_id)
                provider_id=i.provider_id
                i.product_price=float(i.product_price)*100
                send_product_information=i
                
            for j in provider_info:
                send_provider_info=j  
            YOUR_ID='rzp_test_RDvbeWiAcblyiP'
            YOUR_SECRET='Zltsh8eeYsLDrXkAMItA7lXM'
            client_order = razorpay.Client(auth=(YOUR_ID, YOUR_SECRET))
            data_order = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
            payment = client_order.order.create(data=data_order)
            return render(res,'payment.html',{'id':payment,'send_product':send_product_information,'send_provider':send_provider_info,'persnal_name':personal_information[0],'persnal_email':personal_information[2],'persnal_contact':personal_information[3],"pid":provider_id,"proid":res.GET['product_id']})





def login_user(res):
    obj=logincheck()
    ok=obj.checkuser(res.POST['email'],res.POST['pas'])
    if ok:
        res.session['username']=res.POST['email']
        res.session['passwprd']=res.POST['pas']
        m=Userlogin.objects.get(Email=res.POST['email'])#.get(id)
        res.session['userid']=m.id
        res.session['name']=m.name
        print(res.session.get('username'))
        return redirect('http://127.0.0.1:8000/indexpage') 
    else:
        return render(res,'login.html')   




def chatapp(res):
    data=[1,2]
    if 'userid' in res.session:
        
        if "chatid"  in res.GET:
            
            checkcontact=chat_contact.objects.filter(from_contact=res.session.get('userid'),to_contact=res.GET['chatid'])
            c=len(checkcontact)
            if c==0 and int(res.session.get('userid'))!=int(res.GET['chatid']):
                nameofuser=Userlogin.objects.filter(id=res.GET['chatid']).values('name')
                chat_contact(from_contact=res.session.get('userid'),to_contact=res.GET['chatid'],name_of_contact=nameofuser).save()
                chat_contact(from_contact=res.GET['chatid'],to_contact=res.session.get('userid'),name_of_contact=res.session.get('name')).save()
 
            
        user_id=res.session.get('userid')
        contact=chat_contact.objects.filter(from_contact=user_id)
        name_list=[]
        name={}
        contact=list(contact)
        for i in contact:
            name={}
            name['username']=(i.name_of_contact)
            name['ids']=(i.to_contact)
            name_list.append(name)
        return render(res,'chat.html',{'data':data,'contact':name_list})
    else:
        return redirect('http://127.0.0.1:8000/loginpage')


def sign_up_perform(res):
    if 'userid' not in res.session:
        obj=sign_up()
        ok=obj.check_not_allready(res.POST['email'],res.POST['password'])
        print(ok)
        if ok:
            new=Userlogin(Email=res.POST['email'],password=res.POST['password'],name=res.POST['Username'],city=res.POST['address'],village_post=res.POST['address2'],contact=res.POST['contact'])
            new.save() 
            res.session['username']=res.POST['email']
            res.session['passwprd']=res.POST['password']
            m=Userlogin.objects.get(Email=res.POST['email'])
            res.session['userid']=m.id
            return redirect('http://127.0.0.1:8000/indexpage')
        else:
            return redirect('http://127.0.0.1:8000/signup')    
    else:
        return redirect('http://127.0.0.1:8000/indexpage')
def sign_up_page(res):
    if 'userid' not in res.session:
        return render(res,'signup.html')
    else:
        return redirect('http://127.0.0.1:8000/indexpage')
        
    
def delete_session(res):
    try:
        del res.session['username']
        del res.session['passwprd']
        del res.session['userid'] 
    except:
        pass
    return redirect('http://127.0.0.1:8000')
def cartpage(res):
    if 'username' in res.session:
        all_cart_info=[]
        random={}
        total=0
        
        
        cart=add_to_cart.objects.filter(who_is_to_add_id=res.session.get('userid'))
        for i in cart:
            image=Product_info.objects.filter(id=i.product_id)
            random['ids']=i.id
            random['name']=i.product_name
            random['price']=i.product_price
            total=total+i.product_price
            # for img in image:
            random['image']=str(image[0].product_image)
            random['product_id']=i.product_id
            all_cart_info.append(random)
            print(random['image']) 
            random={} 
             
            
            
            
            
            
        
        return render(res,'cart.html',{'cart_data':all_cart_info,'total':total,'total_item':len(all_cart_info)})


def ad_to_cart(res):
    print(res.GET['name'])
    add=add_to_cart(product_name=res.GET['name'],product_price=res.GET['price'],product_id=res.GET['id'],who_is_to_add_id=res.session.get('id'))
    add.save()
    return  redirect('http://127.0.0.1:8000/indexpage')

    
            
def chat_contact_list(res):
    p=Product_info.objects.filter(id=1)
    print(p)
    r=''
    for i in p:
        r=i
    all_cart_info=[]
    random={}
    sta=status=Userlogin.objects.filter(id=res.session.get('userid')).values('contact')[0]
    print(sta.get('contact'))    
        
    cart=add_to_cart.objects.filter(who_is_to_add_id=res.session.get('userid'))
    for i in cart:
        image=Product_info.objects.filter(id=i.product_id)
        random['name']=i.product_name
        random['price']=i.product_price
        # for img in image:
        random['image']=image[0].product_image
        random['product_id']=i.product_id
        all_cart_info.append(random)
        random={}   
    print(all_cart_info)     
    return HttpResponse(str(r.id)+r.product_name)
def chat_messages_list(res):
    to_id=res.POST['to_id']
    from_id=res.session.get('userid')
    all_message=chat_messages.objects.filter(from_id=from_id,to_id=to_id).values('messages')
    
    
def jsondata_get(res):
    
    d=res.GET['idname']
    contact_or_chat=res.GET['check']
    if 'userid' in res.session:
        l=[]
        name={}
        get_all_chat=chat_messages.objects.filter(from_id=res.session.get('userid'),to_id=d)|chat_messages.objects.filter(from_id=d,to_id=res.session.get('userid'))
        get_all_chat=list((get_all_chat))
        for i in get_all_chat:
            name={}
            name['message']=(i.message)
            name['to_id']=(i.to_id)
            l.append(name)
        
        data=[1,2,3,4,5,6,7,8,9]
        return JsonResponse({'name':data,'ids':d,'msg':l})
    elif contact_or_chat=='message':
        to_name=res.GET['nameto']
        msg=res.GET['msgdata']
        msg=msg+str(res.session.get('userid'))
        chat_messages(from_name=res.session.get('name'),from_id=res.session.get('userid'),message=msg,to_name=to_name,to_id=d,time_of=datetime.datetime.now()).save()
        
        
        get_all_chat=chat_messages.objects.filter(from_id=1,to_id=d).values('message')
        print(get_all_chat)
        data=[1,2,3,4,5,6,7,8,911,12,34,56,67,78,]
        return JsonResponse({'name':data,'ids':d,'msg':list(get_all_chat)})
           
def justsend(res):
    d=res.GET['idnm']
    to_name=res.GET['nameto']
    msg=res.GET['msgdata']
    msg=msg+str(res.session.get('userid'))
    #chat_messages(from_name=res.session.get('name'),from_id=d,message=msg,to_name=to_name,to_id=res.session.get('userid'),time_of=datetime.datetime.now()).save()
    chat_messages(from_name=res.session.get('name'),from_id=res.session.get('userid'),message=msg,to_name=to_name,to_id=d,time_of=datetime.datetime.now()).save()

    return JsonResponse({'ok':'ok'});    
def deletecart(res):
    delete= int(res.GET['deleteid']) 
    status=add_to_cart.objects.filter(id=delete).delete()#,who_is_to_add_id=res.session.get('userid')).delete()
    
    print(status)
    if status:
        return JsonResponse({'stat':'ok'})
    else:
        return JsonResponse({'stat':'not'})

       
def Transaction_history(res):
    to_id= res.session.get('userid')       
    from_id= res.Get['from_id']
    orderid=  res.Get['orderid']
    signature=res.GET['signature']
    paymentid=res.Get['pay_id']
    productid=res.Get['product_id']
    paymentHistory.payment_id=paymentid
    paymentHistory.order_id=orderid
    paymentHistory.signature=signature
    paymentHistory.payment_id=productid
    paymentHistory.Buy_to_id=to_id
    paymentHistory.sold_to_id=from_id
    Product_info.objects.filter(id=productid).update(status="True")
    paymentHistory.save()
    
def myproduct(res):    
    myid=res.session.get('userid')
    data=Product_info.objects.filter(provider_id=1).values()
    print(data)
    return render(res,'myproduct.html',{'data':data})#,"myname":personal_information[0],"myemail":personal_information[1],"myid":personal_information[2]})
def delete_my_item(res):
    delete= int(res.GET['delete']) 
    status=Product_info.objects.filter(id=delete).delete()#,who_is_to_add_id=res.session.get('userid')).delete()
    
    print(status)
    if status:
        return JsonResponse({'stat':'ok'})
    else:
        return JsonResponse({'stat':'not'})
        
def addproduct(res):
    try:
        if "userid" in res.session:
            pass
        else:
            return redirect('http://127.0.0.1:8000/')
        name=res.POST['name']
        price=res.POST['price']
        image=res.FILES['imge']
        cat=res.POST['cat'] 
   
        provide=res.session.get('userid')
        brand=res.POST['brand']  
        status="false"
        Product_info.product_brand=brand
        Product_info.product_cat=cat
        Product_info.product_image=image
        Product_info.product_name=name
        Product_info.product_price=price
        Product_info.provider_id=provide
        Product_info.status=status
        Product_info.save()
        return redirect('http://127.0.0.1:8000/My-product')
    except Exception as e:
        return HttpResponse(e)
    
        
    
    
                                                                                                                                                          