class pohonSimpul:
    def __init__(obj, data):
        obj.data = data
        obj.children = []
        obj.parent = None
    def get_level(obj):
        level = 0
        p = obj.parent
    while p:
        level += 1
        p = p.parent

    return level
    def print_tree(obj):
        spaces = ' ' * obj.get_level() * 3
        prefix = spaces + "|__" if obj.parent else ""
        print(prefix + obj.data)
        if obj.children:
            for child in obj.children:
                child.print_tree()
    
    def add_child(obj, child):
        child.parent = obj
        obj.children.append(child)
    
def build_mobil_tree():
    root = pohonSimpul("JenisMobilil")
    konvensional = pohonSimpul("Konvensional")
    konvensional.add_child(pohonSimpul("Avanza"))
    konvensional.add_child(pohonSimpul("Brio"))
    konvensional.add_child(pohonSimpul("Agya"))
    konvensional.add_child(pohonSimpul("Ayla"))

    hybrid = pohonSimpul("Hybrid")
    hybrid.add_child(pohonSimpul("XL 7"))
    hybrid.add_child(pohonSimpul("Inova Venturer"))
    hybrid.add_child(pohonSimpul("Ertiga Hybrid"))
    hybrid.add_child(pohonSimpul("Inova Venturer"))
    hybrid.add_child(pohonSimpul("Ertiga Hybrid"))
    
    electrik= pohonSimpul("Electrik")
    electrik.add_child(pohonSimpul("Ioniq 5"))
    electrik.add_child(pohonSimpul("Mini Ev"))
    electrik.add_child(pohonSimpul("Tesla S"))
    electrik.add_child(pohonSimpul("Hyundai Kona"))
    electrik.add_child(pohonSimpul("Outlander PHEV"))
    electrik.add_child(pohonSimpul("Lexus UX300"))
    
    root.add_child(konvensional)
    root.add_child(hybrid)
    root.add_child(electrik)
    root.print_tree()
if __name__ == '__main__':
    build_mobil_tree()


