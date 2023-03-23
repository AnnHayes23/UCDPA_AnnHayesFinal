import enum


class Region(enum.Enum):
    C = 'Connacht'
    L = 'Leinster'
    M = "Munster"
    U = 'Ulster'


class County(enum.Enum):
    CL = 'Clare', Region.M
    C = 'Cork', Region.M
    KY = 'Kerry', Region.M
    LK = 'Limerick', Region.M
    T = 'Tipperary', Region.M
    W = 'Waterford', Region.M

    CW = 'Carlow', Region.L
    D = 'Dublin', Region.L
    KE = 'Kildare', Region.L
    KK = 'Kilkenny', Region.L
    LS = 'Laois', Region.L
    LD = 'Longford', Region.L
    LH = 'Louth', Region.L
    MH = 'Meath', Region.L
    OY = 'Offaly', Region.L
    WH = 'Westmeath', Region.L
    WW = 'Wicklow', Region.L
    WX = 'Wexford', Region.L

    G = 'Galway', Region.C
    LM = 'Leitrim', Region.C
    MO = 'Mayo', Region.C
    RN = 'Roscommon', Region.C
    SO = 'Sligo', Region.C

    CN = 'Cavan', Region.U
    MN = 'Monaghan', Region.U
    DL = 'Donegal', Region.U
