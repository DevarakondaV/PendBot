from boot import do_connect
if (do_connect()):
    import page
else:
    print("Not Connected")
