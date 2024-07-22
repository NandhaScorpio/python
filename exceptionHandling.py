try :
    a =int(input())
    b =int(input())

except ValueError as e:
    print("Value Error :",e)

except Exception as e :
    print("Something Wrong :",e)

finally :
    print("Done")
