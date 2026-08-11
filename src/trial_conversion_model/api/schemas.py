from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """One trial's first-3-day base aggregates, as the caller knows them."""

    # TODO: declare the seven fields a caller must send, one line each,
    # with a type for each. They are the same seven base aggregates your
    # feature code starts from; features.py names them.


class PredictionResponse(BaseModel):
    """What we send back: a probability and a band a human can act on."""

    # TODO: declare the two fields the caller gets back: the conversion
    # probability, and the low/medium/high band it falls in.
