# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:38:28 2021

@author: İbrahim
"""
# Company Adında Şirket Sınıfı Oluşturuldu.
class Company:
    # Şirket Çalışanlaarının Bilgileri Referans Kullanılarak alındı
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = name+surname + '@icloud.com'
    # Şirket Çalışanlarının Bilgileri ShowInfo methodunda salkandı.
    def showInfo(self):
        return f'Name : {self.name} \n Surname: {self.surname} \n Age : {self.age}\nEmail : {self.email}'
    # Yönetici Sınıfı Oluşturuldu
class ExeCutive(Company):
    def __init__(self,name,surname,age,employes=None):
        # super methodu ile var olan bilgileri tekrar yazmayarak 
        #Şirket sınıfından referans alındı
        super().__init__(name,surname,age)
       # Eğer Yöneticiye Bağlı Çalışan Yoksa Boş liste oluşturulacak
        if employes == None:
            self.employes = []
        # Eğer Yöneticiye ait çalışan varsa self.employes  = employes olarak dışarıdan 
        # girilen çalışan employes'e atanacak
        else:
            self.employes = employes
        # yöneticinin çalışan eklemesi için add_employes methodu oluşturuldu.
    def add_employes(self,employes):
        # Eğer dışarıdan girilen employes employes listesinin 
        #içinde yoksa self.employes.append(employes) ile listeye eklenecek
        if employes not in self.employes:
            self.employes.append(employes)
        else:
            pass
        # Yöneticinin Çalışanı işten Çıkarması için remove_employes methodu oluşturuldu.
    def remove_employes(self,employes):
        # Eğer employes listesinin içinde silinmesi gereken 
        #çalışan varsa self.employes.remove ile çalışan liseteden çıkarılacak
        if employes in self.employes:
            self.employes.remove(employes)
        else:
            pass

