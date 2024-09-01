class SarkException(Exception):
    pass


class SarkError(SarkException):
    pass


class SarkNoSelection(SarkError):
    pass


class SarkNoFunction(SarkError):
    pass


class SarkAddFunctionFailed(SarkError):
    pass


class SarkFunctionExists(SarkError):
    pass


class SarkStructError(SarkError):
    pass


class SarkInvalidRegisterName(SarkError):
    pass


class SarkStructAlreadyExists(SarkStructError):
    pass


class SarkStructCreationFailed(SarkStructError):
    pass


class SarkStructNotFound(SarkStructError):
    pass


class SarkTerr(SarkError):
    value: int
    msg: str

    @staticmethod
    def get_terr_class(value: int) -> "SarkTerr":
        for cls in SarkTerr.__subclasses__():
            if cls.value == value:
                return cls


class SarkTerrSaveError(SarkTerr):
    value = -1
    msg = "failed to save"


class SarkTerrSerialize(SarkTerr):
    value = -2
    msg = "failed to serialize"


class SarkTerrBadName(SarkTerr):
    value = -3
    msg = "name s is not acceptable"


class SarkTerrBadSync(SarkTerr):
    value = -4
    msg = "failed to synchronize with IDB"


class SarkTerrBadArg(SarkTerr):
    value = -5
    msg = "bad argument"


class SarkTerrBadType(SarkTerr):
    value = -6
    msg = "bad type"


class SarkTerrBadSize(SarkTerr):
    value = -7
    msg = "bad size d"


class SarkTerrBadIndex(SarkTerr):
    value = -8
    msg = "bad index d"


class SarkTerrBadArray(SarkTerr):
    value = -9
    msg = "arrays are forbidden as function arguments"


class SarkTerrBadBf(SarkTerr):
    value = -10
    msg = "bitfields are forbidden as function arguments"


class SarkTerrBadOffset(SarkTerr):
    value = -11
    msg = "bad member offset s"


class SarkTerrBadUnivar(SarkTerr):
    value = -12
    msg = "unions cannot have variable sized members"


class SarkTerrBadVarlast(SarkTerr):
    value = -13
    msg = "variable sized member must be the last member in the structure"


class SarkTerrOverlap(SarkTerr):
    value = -14
    msg = "the member overlaps with other members that cannot be deleted"


class SarkTerrBadSubtype(SarkTerr):
    value = -15
    msg = "recursive structure nesting is forbidden"


class SarkTerrBadValue(SarkTerr):
    value = -16
    msg = "value 0xI64X is not acceptable"


class SarkTerrNoBmask(SarkTerr):
    value = -17
    msg = "bitmask 0xI64X is not found"


class SarkTerrBadBmask(SarkTerr):
    value = -18
    msg = (
        "Bad enum member mask 0xI64X. The specified mask should not intersect with any"
    )


class SarkTerrBadMskval(SarkTerr):
    value = -19
    msg = "bad bmask and value combination (value=0xI64X; bitmask 0xI64X)"


class SarkTerrBadRepr(SarkTerr):
    value = -20
    msg = "bad or incompatible field representation"


class SarkTerrGrpNoempty(SarkTerr):
    value = -21
    msg = "could not delete group mask for not empty group 0xI64X"


class SarkTerrDupname(SarkTerr):
    value = -22
    msg = "duplicate name s"


class SarkTerrUnionBf(SarkTerr):
    value = -23
    msg = "unions cannot have bitfields"


class SarkTerrBadTah(SarkTerr):
    value = -24
    msg = "bad bits in the type attributes (TAH bits)"


class SarkTerrBadBase(SarkTerr):
    value = -25
    msg = "bad base class"


class SarkTerrBadGap(SarkTerr):
    value = -26
    msg = "bad gap"


class SarkTerrNested(SarkTerr):
    value = -27
    msg = "recursive structure nesting is forbidden"


class SarkTerrNotCompat(SarkTerr):
    value = -28
    msg = "the new type is not compatible with the old type"


class SarkTerrBadLayout(SarkTerr):
    value = -29
    msg = "failed to calculate the structure/union layout"


class SarkTerrBadGroups(SarkTerr):
    value = -30
    msg = "bad group sizes for bitmask enum"


class SarkTerrBadSerial(SarkTerr):
    value = -31
    msg = "enum value has too many serials"


class SarkTerrAlienName(SarkTerr):
    value = -32
    msg = "enum member name is used in another enum"


class SarkTerrStock(SarkTerr):
    value = -33
    msg = "stock type info cannot be modified"


class SarkTerrEnumSize(SarkTerr):
    value = -34
    msg = "bad enum size"


class SarkTerrNotImpl(SarkTerr):
    value = -35
    msg = "not implemented"


class SarkTerrTypeWorse(SarkTerr):
    value = -36
    msg = "the new type is worse than the old type"


class SarkTerrBadFxSize(SarkTerr):
    value = -37
    msg = "cannot extend struct beyond fixed size"


class SarkEnumError(SarkError):
    pass


class EnumNotFound(SarkEnumError):
    pass


class EnumCreationFailed(SarkEnumError):
    pass


class EnumAlreadyExists(SarkEnumError):
    pass


class CantRenameEnumMember(SarkEnumError):
    pass


class CantSetEnumMemberComment(SarkEnumError):
    pass


class SarkErrorNameAlreadyExists(SarkError):
    pass


class SarkSetNameFailed(SarkError):
    pass


class SarkSwitchError(SarkError):
    pass


class SarkNotASwitch(SarkSwitchError):
    pass


class SarkNoInstruction(SarkError):
    pass


class SarkOperandError(SarkError):
    pass


class SarkOperandWithoutReg(SarkOperandError):
    pass


class CantSetEnumComment(SarkEnumError):
    pass


class CantDeleteEnumMember(SarkEnumError):
    pass


class CantSetEnumBitfield(SarkEnumError):
    pass


class CantRenameEnum(SarkEnumError):
    pass


class SarkGuiError(SarkError):
    pass


class SarkMenuError(SarkGuiError):
    pass


class MenuAlreadyExists(SarkMenuError):
    pass


class MenuNotFound(SarkMenuError):
    pass


class FormNotFound(SarkGuiError):
    pass


class InvalidStructOffset(SarkStructError):
    pass


class SegmentError(SarkError):
    pass


class NoMoreSegments(SegmentError):
    pass


class InvalidBitness(SegmentError):
    pass


class NoFileOffset(SarkError):
    pass


class SarkNoString(SarkError):
    pass


class SarkExpectedPatchedByte(SarkError):
    pass


class PhraseError(SarkOperandError):
    pass


class OperandNotPhrase(PhraseError):
    pass


class InvalidPhraseRegisters(PhraseError):
    pass


class PhraseNotSupported(PhraseError):
    pass


class PhraseProcessorNotSupported(PhraseNotSupported):
    pass


class SetTypeFailed(SarkError):
    def __init__(self, ea, c_signature):
        message = 'idc.SetType(ea={ea:08X}, "{c_signature}") failed'.format(
            ea=ea, c_signature=c_signature
        )
        super(SetTypeFailed, self).__init__(message)
