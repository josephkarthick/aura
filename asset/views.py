from django.shortcuts import render,redirect
from asset.models  import it_asset
from django.http      import HttpResponse
from reportlab.pdfgen import canvas
from asset.models   import voip, cred
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import openpyxl
import pdfrw





def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = cred.objects.get(emp_id=username)
            
            if user.password == password:
                if user.dept == 'IT':
                    return redirect('home')
                else:
                    messages.error(request,'Use Emp Login')
            else:
                messages.error(request,'Invalid username Password')
        except cred.DoesNotExist:
            messages.error(request,'Authendication Failed')
            
    return render(request,'login.html', {'msg': messages.get_messages(request)})        


def logout_view(request):
    logout(request)
    return redirect('login')
    

def home(request):
    
    mon           = it_asset.objects.filter(assetname='monitor')
    monitor       = it_asset.objects.filter(assetname='monitor').count
    usedmonitor   = it_asset.objects.filter(assetname='monitor', condition='used').count
    stkmonitor    = it_asset.objects.filter(assetname='monitor', condition='stock').count
    srpmonitor    = it_asset.objects.filter(assetname='monitor', condition='Scrap').count

    cpu       = it_asset.objects.filter(assetname='cpu').count
    usedcpu   = it_asset.objects.filter(assetname='cpu', condition='used').count
    stkcpu    = it_asset.objects.filter(assetname='cpu', condition='stock').count
    srpcpu    = it_asset.objects.filter(assetname='cpu', condition='Scrap').count

    keys       = it_asset.objects.filter(assetname='keyboard')
    keyboard   = it_asset.objects.filter(assetname='keyboard').count
    usedkeys   = it_asset.objects.filter(assetname='keyboard', condition='used').count
    stkkeys    = it_asset.objects.filter(assetname='keyboard', condition='stock').count
    srpkeys    = it_asset.objects.filter(assetname='keyboard', condition='Scrap').count
            
    mouse       = it_asset.objects.filter(assetname='mouse').count        
    usedmouse   = it_asset.objects.filter(assetname='mouse', condition='used').count
    stockmouse  = it_asset.objects.filter(assetname='mouse', condition='stock').count
    srpmouse    = it_asset.objects.filter(assetname='mouse', condition='scrap').count
    
    headset      = it_asset.objects.filter(assetname='headset').count
    usedheadset  = it_asset.objects.filter(assetname='headset',  condition='used').count
    stockheadset = it_asset.objects.filter(assetname='headset', condition='stock').count
    srpheadset   = it_asset.objects.filter(assetname='headset',   condition='scrap').count
    
    sip     = voip.objects.all().count
    pulse   = voip.objects.filter(vendor='pulse').count
    siplink = voip.objects.filter(vendor='siplink').count
    skyfall = voip.objects.filter(vendor='skyfall').count
    unified = voip.objects.filter(vendor='unified').count
    
    usdvoip = voip.objects.filter(status='used').count
    freevoip= voip.objects.filter(status='not used').count
    
    context = {
               'cpu' : cpu, 'usedcpu':usedcpu, 'stkcpu':stkcpu, 'srpcpu':srpcpu,
               'monitor' : monitor, 'usedmonitor':usedmonitor, 'stkmonitor':stkmonitor, 'srpmonitor':srpmonitor,
               'keys' : keyboard, 'usedkeys':usedkeys, 'stkkeys':stkkeys, 'srpkeys':srpkeys, 
               'mouse': mouse, 'usedmouse':usedmouse, 'stockmouse':stockmouse,
               'sip' : sip, 'pulse': pulse, 'siplink' : siplink, 'skyfall' : skyfall, 'unified' : unified,
               'headset' : headset, 'usedheadset' : usedheadset, 'stockheadset' : stockheadset, 'srpheadset' : srpheadset,
               'usdvoip': usdvoip, 'freevoip' : freevoip, 
              }
    return render(request, 'index.html', context)
    
    
    
def itassetlist(request):
        assetdata = it_asset.objects.all()
        return render(request, 'itassetlist.html', {'asdata':assetdata})
    
def add_asset(request):
    if request.method == "POST":
        asname   =   request.POST   ['asname'].Title()
        asid     =   request.POST   ['asid'].Title()
        ascat    =   request.POST   ['ascat'].Title()
        pdate    =   request.POST   ['pdate'].Title()
        pfrom    =   request.POST   ['pfrom'].Title()
        manft    =   request.POST   ['manft'].Title()
        model    =   request.POST   ['model'].Title()
        sno      =   request.POST   ['sno'].Title()
        sup      =   request.POST   ['sup'].Title()
        cnd      =   request.POST   ['cnd'].Title()
        wrnty    =   request.POST   ['wrnty'].Title()
        value    =   request.POST   ['value'].Title()
        dayuser  =   request.POST   ['dayuser'].Title()
        nightuser=   request.POST   ['nightuser'].Title()
        gby      =   request.POST   ['gby'].Title()
        dsts     =   request.POST   ['dsts'].Title()
        ddate    =   request.POST   ['ddate'].Title()
        des      =   request.POST   ['des'].Title()
        
        
        qry = it_asset.objects.create(  assetname=asname,  assetID=asid, assetcat=ascat, purchasedate=pdate,  purchasefrom=pfrom,  manufacturer=manft,  model=model,
                                    serialno=sno, supplier=sup,   condition=cnd,  warranty=wrnty,   value=value,  dayuser=dayuser, nightuser=nightuser,  givenby=gby,
                                    Dstatus=dsts, Ddate=ddate, description=des)
        qry.save()
    return render(request, 'add_asset.html')
    
def editasset(request):
    assetdata = it_asset.objects.all()
    return render (request, 'editasset.html', {'asdata':assetdata})
    
def edit_asset(request,sno):
    data = it_asset.objects.get(sno = sno)
    if request.method == "POST":
        data.assetname         =   request.POST   ['asname'].Title()
        data.assetID           =   request.POST   ['asid'].Title()
        data.assetcat          =   request.POST   ['ascat'].Title()
        data.purchasedate      =   request.POST   ['pdate'].Title()
        data.purchasefrom      =   request.POST   ['pfrom'].Title()
        data.manufacturer      =   request.POST   ['manft'].Title()
        data.model             =   request.POST   ['model'].Title()
        data.serialno          =   request.POST   ['sno'].Title()
        data.supplier          =   request.POST   ['sup'].Title()
        data.condition         =   request.POST   ['cnd'].Title()
        data.warranty          =   request.POST   ['wrnty'].Title()
        data.value             =   request.POST   ['value'].Title()
        data.dayuser           =   request.POST   ['dayuser'].Title()
        data.nightuser         =   request.POST   ['nightuser'].Title()
        data.givenby           =   request.POST   ['gby'].Title()
        data.Dstatus           =   request.POST   ['dsts'].Title()
        data.Ddate             =   request.POST   ['ddate'].Title()
        data.description       =   request.POST   ['des'].Title()
        data.save()
        return redirect (itassetlist)
    return render(request,'edit_asset.html', {'data':data})

def delasset(request,sno):
    data = it_asset.objects.get(sno=sno)
    data.delete()
    return redirect(itassetlist)
    
def search(request,sno):
    results = it_asset.objects.filter(assetname=sno)  # Replace `name` with the field you want to search on
    context = {'results': results}
    return render(request, 'itassetlist.html', context)
    
def addvoip(request):
    if request.method == 'POST':
        vendor      =  request.POST ['vendor']
        cbn         =  request.POST ['cbn']
        usrno       =  request.POST ['usrno']
        domain      =  request.POST ['domain']
        psw         =  request.POST ['psw']
        username    =  request.POST ['user']
        dop         =  request.POST ['date']
        remarks     =  request.POST ['remarks']
        status      =  request.POST ['status']
        
        data = voip.objects.create( vendor = vendor, callbacknumber = cbn, usernumber = usrno, domain  = domain, password = psw, username = username, dop = dop, remarks = remarks, status = status    )
        data.save()
    return render(request, 'add-voip.html')
    
def voiplist(request):
    voiplist = voip.objects.all()
    return render (request, 'voiplist.html', {'voip' : voiplist})

def editvoip(request):
    voipdata = voip.objects.all()
    return render (request, 'editvoip.html', {'voipdata' : voipdata})

    
def edit_voip(request,sno):
    voipdata = voip.objects.get(id = sno)
    if request.method == "POST":
        voipdata.vendor             = request.POST['vendor']
        voipdata.callbacknumber     = request.POST['cbn']
        voipdata.usernumber         = request.POST['usrno']
        voipdata.domain             = request.POST['domain']
        voipdata.password           = request.POST['psw']
        voipdata.username           = request.POST['user']
        voipdata.dop                = request.POST['date']
        voipdata.remarks            = request.POST['remarks']
        voipdata.status             =  request.POST ['status']
        voipdata.save()
        return redirect (voiplist)
    return render(request, 'edit_voip.html', {'sip' : voipdata})   

def delvoip(request,sno):
    data = voip.objects.get(id=sno)
    data.delete()
    return redirect(voiplist)    
    


def download_excel(request):
    # ... your existing code to fetch data from the database
    data = it_asset.objects.all()
    # Create a new Excel workbook and add data to it
    wb = openpyxl.Workbook()
    ws = wb.active   
      
    
    ws.append(['ASSETNAME','ASSETID','ASSETCAT'   ,'PURCHASE DATE','PURCHASE FROM','MANUFACTURE','MODEL','SUPPLIER'  ,'CONDITION' ,'WARRANTY' ,'VALUE'  ,'DAY USER'    ,'NIGHT USER'  ,'GIVEN BY' ])
    for item in data:
        ws.append([item.assetname,item.assetID,item.assetcat])
   
    # Save the workbook to response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data.xlsx'
    wb.save(response)

    return response
    
    
def voip_ex(request):
    # ... your existing code to fetch data from the database
    voip_data = it_voip.objects.all()
    # Create a new Excel workbook and add data to it
    wb = openpyxl.Workbook()
    ws = wb.active   
      
    
    ws.append(['No','Vendor','Call Back Number','User Name','Domain','Password','End User','DOP','Remarks','Status'])
    for data in voip_data:
        ws.append([data.vendor,data.callbacknumber,data.usernumber,data.domain,data.password,data.username,data.dop,data.remarks,data.status])
   
    # Save the workbook to response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=voipdata.xlsx'
    wb.save(response)

    return response    

#def pdf(request, sno):
#    try:
#        # Fetch data from the database based on sno
#        pdfdata = it_asset.objects.get(sno=sno)
#
#        # Path to your fillable PDF form
#        pdf_form_path = 'static/file/asset.pdf'
#
#        # Read the PDF form
#        pdf_data = pdfrw.PdfReader(pdf_form_path)
#        annotations = pdf_data.pages[0]['/Annots']
#
#        # Fill form fields with data from the database
#        for annotation in annotations:
#            if '/T' in annotation and '/V' in annotation:
#                field_name = annotation['/T'][1:-1]  # Get field name without '/'
#                if field_name == '/Text1':
#                    annotation.update(pdfrw.PdfDict(V=f'{pdfdata.assetname}'))
#                elif field_name == 'Text2':
#                    annotation.update(pdfrw.PdfDict(V=f'{pdfdata.assetcat}'))
#
#
#        # Create a response object with the filled PDF content
#        response = HttpResponse(content_type='application/pdf')
#        response['Content-Disposition'] = f'attachment; filename="{pdfdata.assetname}_report.pdf"'
#
#        # Write the filled PDF content to the response object
#        pdfrw.PdfWriter().write(response, pdf_data)
#
#        return response
#
#    except it_asset.DoesNotExist:
#        # Handle the case where the provided sno does not exist in the database
#        return HttpResponse("Record not found for the given sno.")
#    except Exception as e:
#        # Handle other exceptions
#        print("Error:", str(e))
#        return HttpResponse("An error occurred while generating the PDF.")



def pdf(request, sno):
    try:
        # Fetch data from the database based on sno
        pdfdata = it_asset.objects.get(sno=sno)

        # Create a response object
        response = HttpResponse(content_type='application/pdf')
        
        # Set the Content-Disposition header to force download the PDF file
        response['Content-Disposition'] = f'attachment; filename="{pdfdata.assetname}_report.pdf"'

        # Create a PDF object using the response object as its file
        p = canvas.Canvas(response)

        # Write the data from the database to the PDF
        p.drawString(250, 800, f'{pdfdata.assetname} : Report')
        p.drawString(50, 750, f'Asset Name: {pdfdata.assetname}')
        p.drawString(50, 730, f'Asset Category: {pdfdata.assetcat}')
        p.drawString(50, 710, f'Purchase Date: {pdfdata.purchasedate}')

        # Close the PDF object cleanly, and we're done
        p.showPage()
        p.save()

        return response

    except it_asset.DoesNotExist:
        # Handle the case where the provided sno does not exist in the database
        return HttpResponse("Record not found for the given sno.")
    except Exception as e:
        # Handle other exceptions
        print("Error:", str(e))
        return HttpResponse("An error occurred while generating the PDF.")






 
    

    
    

