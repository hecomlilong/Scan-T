#!/usr/bin/python
#coding:utf-8
import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self,req,fp,code,msg,headers):
		print '301问题'
	def http_error_302(self,req,fp,code,msg,headers):
		print '302问题'
def formatstring(str):
	return '\''+str+'\''
def setCookies(response,user,time):
	response.set_cookie('islogin',user.islogin,time)
	response.set_cookie('username',user.username,time)
	response.set_cookie('role',user.role,time)
	response.set_cookie('power',user.power,time)
def delCookies(response):
	response.delete_cookie('islogin')
	response.delete_cookie('username')
	response.delete_cookie('role')
	response.delete_cookie('power')
#convert object to a dict
def object2dict(obj):
	d = {}
	d['__class__'] = obj.__class__.__name__
	d['__module__'] = obj.__module__
	d.update(obj.__dict__)
	return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst
	
	
	