from django.shortcuts import render
from django.views.generic import View
from base import models as base_model

# Create your views here.

class mainView(View):
    def get(self,request):
        cu = base_model.country.objects.all()
        gt = base_model.gotypes.objects.all()
        # ag = getagancy_byname('Odyssey  Group')
        # ag = getagancy_byid(1)
        # ag = createPname('گروه مهاجرتی ادیسه')
        return render(request,'base/main.html',{'cu':cu,'gt':gt})
    def post(self,request):
        ag = getagancy_byname(request.POST['name'])
        print('---------------------------')
        print(ag)
        agsim = findsimilar_byname(request.POST['name'])
        cu = base_model.country.objects.all()
        gt = base_model.gotypes.objects.all()
        return render(request,'base/main.html',{'ag':ag,'cu':cu,'gt':gt,'agsim':agsim})

class bycountryView(View):
    def get(self,request,cu_id,page):
        country = getcountry_byid(cu_id)
        agVcu_list = getagancies_bycup(country,page)

        return render(request , 'base/listingpage.html' , {'cu':country , 'ag_list':agVcu_list})


def getagancy_byid(ag_id):
    try:
        agancy = base_model.baseagancy.objects.get(id = ag_id )
    except:
        agancy = 'none'

    if agancy == 'none':
        return 'error:there is not agancy by this id'
    else:
        return agancy

def getagancy_byname(ag_name):
    ag_n = str(ag_name)
    ag_cn = createPname(ag_name)
    try:
        if base_model.baseagancy.objects.filter(Pname=ag_n).exists():
            agancy = base_model.baseagancy.objects.get(Pname=ag_n)
            return agancy
        elif base_model.baseagancy.objects.filter(Ename = ag_n.title()).exists():
            agancy = base_model.baseagancy.objects.get(Ename = ag_n.title())
            return agancy
        elif ag_cn != 'error':
            agancy_list = base_model.baseagancy.objects.all()
            for ag in agancy_list:
                if ag_cn in ag.Pname:
                    return ag
                elif ag_cn in ag.Ename.lower():
                    return ag
                else:
                    return 'error'
                

            
            
        else:
            return 'error'

    except:
        return 'error'


def createPname(basestring):
    basic_words = ['مهاجرتی','مهاجرت','گروه','موسسه','آژانس','اژانس','شرکت']
    basic_ewords = ['agancy','immigrate','immigration','group','groups','company']
    try:
        ag_name = str(basestring).lower()
        lvl1 = ag_name.strip()
        for bs in basic_words:
            if bs in lvl1:
                lvl1 = lvl1.replace(str(bs),'')
                lvl1 = lvl1.strip()
        for bs in basic_ewords:
            if bs in lvl1.lower():
                lvl1 = lvl1.replace(str(bs),'')
                lvl1 = lvl1.strip()

        return lvl1
    except:
        return 'error'

def findsimilar_byname(basestring):
    try:
        ag_name = createPname(basestring)
        agancies = base_model.baseagancy.objects.all()
        true_similar_p_list = []
        true_similar_e_list = []
        similar_p_list = []
        similar_e_list = []
        may_similar_p_list = []
        may_similar_e_list = []
            

        for ag in agancies:
            base_pchars = len(ag.base_pname)
            base_echars = len(ag.base_ename)
            true_similar_point_p = int(base_pchars * 0.7) 
            true_similar_point_e = int(base_echars * 0.7)

            similar_point_p = int(base_pchars * 0.5) 
            similar_point_e = int(base_echars * 0.5) 

            may_similar_point_p = int(base_pchars * 0.3)
            may_similar_point_e = int(base_echars * 0.3)
            point_p = 0
            point_e = 0
            for char in str(ag_name):
                if char in ag.base_pname:
                    point_p += 1
                elif  char in ag.base_ename:
                    point_e += 1

            if point_p >= true_similar_point_p:
                true_similar_p_list.append(ag)
            elif point_p >= similar_point_p:
                similar_p_list.append(ag)
            elif point_p >= may_similar_point_p:
                may_similar_p_list.append(ag)

            if point_e >= true_similar_point_e:
                true_similar_e_list.append(ag)
            elif point_e >= similar_point_e:
                similar_e_list.append(ag)
            elif point_e >= may_similar_point_e:
                may_similar_e_list.append(ag)

        return true_similar_p_list , true_similar_e_list , similar_p_list , similar_e_list , may_similar_p_list , may_similar_e_list
    except:
        return 'error'

def getcountry_byid(cu_id):
    try:
        country = base_model.country.objects.get(id = int(cu_id))
        return country
    except:
        return 'error'

def getagancies_bycup(cu , page):
    try:
        end_index = page * 5
        start_index = end_index - 5
        base_list = base_model.agVcu.objects.filter(country = cu).order_by('-point')[start_index:end_index]
        
        return base_list
    except:
        return 'error'


# ____________________________ name pointer to find similar list
# name pointer >> if createPname is similar by base_pname or base_ename by down rate
# 70% or more similar charakter > true similar
# 50% - 69.9% > similar
# -50% may similar
# -30% not similar
