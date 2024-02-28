from logic import *

rain = Symbol("rain") # It is raining.
hagrid = Symbol("hagrid") # Harry visited Hagrid.
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore.

#sentence = And(rain, hagrid)
#
#print(sentence.formula())

#knowledge = Implication(Not(rain), hagrid)
#
#print(knowledge.formula())

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))

class Loan(models.Model):
    """
    A class representing WHOLE (loan + msr) loans for Freedom.

    Omitted fields from Client_Coissue_Tape:
       - transfer
    """
    __str__ = "freedom_loan"

    class Meta:
        app_label = "freedom"

    commitment = JSONField(default=dict, blank=True, null=True)