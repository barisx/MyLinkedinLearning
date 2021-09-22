# demonstrate template string functions

from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're watching {meyaba} by {gitsene}".format(meyaba="Advanced Python", gitsene="Joe Marini")
    print(str1)

    # TODO: create a template with placeholders
    templ = Template("You're watchong ${title} by ${author}")

    # TODO; use the substitute method with keyword arguments
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # TODO: use the substitute method with a dictionary
    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)
    str1 = "You're watching {author} by {title}".format(**data)
    print(str1)
    # https://www.netsparker.com/blog/web-security/format-string-vulnerabilities/
    
if __name__ == "__main__":
    main()
