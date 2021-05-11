from django.shortcuts import render, redirect
from . models import Site_User, Construction_Site, Transaction
from . filters import TransactionFilter
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from . forms import TransactionForm


@login_required
def transactionHomeView(request):
    trans_datas = []
    myFilter = []
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
        trans_datas = Transaction.objects.all()
        myFilter = TransactionFilter(request.GET, queryset=trans_datas)
        trans_datas = myFilter.qs
    return render(request, 'pages/home.html', {'trans_datas': trans_datas, 'myFilter': myFilter, 'form': form})
