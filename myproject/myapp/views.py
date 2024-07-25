from django.shortcuts import render
from .models import University
import requests
from bs4 import BeautifulSoup

def search_universities(request):
    query = request.GET.get('query', '')
    
    url = "https://univerlist.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    university_names = soup.find_all('h4', class_='mb--0')
    university_links = soup.find_all('a', class_='feature')

  
    University.objects.all().delete()  

    for name, link in zip(university_names, university_links):
        university_name = name.get_text(strip=True)
        university_url = link['href']
        if not university_url.startswith('http'):
            university_url = f"https://univerlist.com{university_url}"
        
        University.objects.create(name=university_name, url=university_url)

    
    if query:
        results = University.objects.filter(name__icontains=query)
    else:
        results = University.objects.all()

    
    return render(request, 'index.html', {'results': results})
