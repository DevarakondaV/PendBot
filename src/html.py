#Contains HTML for webpage


html = """
<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Control </title></head>
    <body>
        <h1> ESP8266 Control </h1>
        <table border="1">
            <tr><th align="left">Duty Cycle</th></tr>
            <tr>
                <td>
                    <form>
                    <input type="text" name="Dcycle"></input>
                    <button type="submit" >Go</button> </form>
                </td>
            </tr>        
        </table>
        <h2> Files on ESP </h2>
        <table border="1">
            <tr><th>File name</th></tr> %s </table> 
    </body>
</html>
"""
