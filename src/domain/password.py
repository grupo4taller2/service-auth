from pydantic import BaseModel


class Password(BaseModel):
    text: str

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.text == other.text
