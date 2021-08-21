import requests
url = "https://tms.tpf.go.tz"
data = {
    "service": "LICENCE",
    "vehicle": "T 122 DPJ,",
    "formSig": "1wFnfawEIyibAOqol81pz2ZE13fcDjahf4fRMa%2FF0xk%3D",
}

print(requests.post(url, data).text)
