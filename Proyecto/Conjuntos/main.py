from model.set_model import SetModel
from model.relation_model import RelationModel
from view.set_view import SetView
from controller.controller import Controller


def main():
    set_model = SetModel()
    relation_model = RelationModel(universe={"a", "b", "c"})  # universo de ejemplo
    view = SetView()
    Controller(set_model, relation_model, view)
    view.mainloop()


if __name__ == "__main__":
    main()
