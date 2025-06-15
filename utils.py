print('Running Lint')
print('Here is an example of line too long ............................................................................................................................................... this might show up in the lint score ....................................................................... and it should show an error')

a = True

if a is True:
  print("1")
  if a is True:
    print("1")
    if a is True:
      print("1")
      if a is True:
        print("1")
      else:
        print("2")
    else:
      print("2")
  else:
    print("2")
else:
  print("2")
