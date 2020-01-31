import sys
# append the freecad libraries to PATH so we can use them
sys.path.append('/usr/lib/freecad/lib')


def main():
    # importing freecad libs for use encapsulated by main
    # so that things such as autopep8 do not force it above
    # appending the system path with their location
    import FreeCAD as app
    import FreeCADGui as gui
    import Part as part
    import Sketcher as sketcher


if __name__ == "__main__":
    main()
