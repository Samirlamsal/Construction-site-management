from django.shortcuts import render, redirect
from . models import Site_User, Construction_Site, Transaction
from . filters import TransactionFilter
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from . forms import TransactionForm
from django.contrib.auth.models import User
import xlwt
from django.http import HttpResponse
from django.utils.timezone import datetime


def UltimateHomeView(request):
    return redirect('/accounts/login/')


@login_required
def transactionHomeView(request):
    trans_datas = []
    myFilter = []
    username = request.user.site_user.name
    workplace = Construction_Site.objects.filter(superviser__name=username)
    if request.method == 'POST':
        data = {
            'trans_user': request.user.site_user,
            'amount': request.POST['amount'],
            'trans_site': request.POST['trans_site'],
            'trans_method': request.POST['trans_method'],
            'comments': request.POST['comments']
        }
        form = TransactionForm(data)
        if form.is_valid():
            form.save()
        return redirect('/transaction_home/')
    else:
        form = TransactionForm()

        trans_datas = Transaction.objects.filter(trans_user__name=username)
        myFilter = TransactionFilter(request.GET, queryset=trans_datas)
        trans_datas = myFilter.qs
    return render(request, 'pages/home.html', {'trans_datas': trans_datas, 'myFilter': myFilter, 'form': form, 'workplace': workplace})


@login_required
def constructionHomeView(request):
    construction_detail = Construction_Site.objects.all()
    return render(request, 'pages/constructionpage.html', {'construction_detail': construction_detail})


@login_required
def export_users_xls(request):
    today_date = datetime.today()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Transaction_Ledger' + \
        str(today_date) + '.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('BuyAndSells')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['TRANSACTION ID', 'AMOUNT', 'STATUS', 'TRANS TYPE',
               'SUBMITTED BY', 'CONSTRUCTION SITE', 'DATE', 'COMMENTS']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Transaction.objects.all().values_list('id', 'amount', 'confirmation_status',
                                                 'trans_type', 'trans_user__fullname', 'trans_site__name', 'trans_date', 'comments')

    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x,
                                                        datetime) else x for x in row] for row in rows]

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if row[2] == True:
                row[2] = 'Confirmed'
            elif row[2]:
                row[2] = 'Not Confirmed'

            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response
