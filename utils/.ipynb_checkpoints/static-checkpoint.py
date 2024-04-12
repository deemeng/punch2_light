# different text color for different situations.
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
    
    
class type_dataset:
    
    ALL = 'all'
    IDRONLY = 'idrOnly'
    SMOOTH_ALL = 'smooth_all'
    SMOOTH_IDRONLY = 'smooth_idrOnly'
    ALL_FD = 'withFullyDisorder'
    ALL_FD_78 = 'withFullyDisorder78'
    
    type_dataset_info = {
        'all': 'no smoothing, all 30% entities', 
        'idrOnly': 'no smoothing, only entities contain IDRs', 
        'smooth_all': 'smoothing, all entities', 
        'smooth_idrOnly': 'smoothing, only entities contain IDRs',
        'withFullyDisorder': 'all 30% dataset + fully disordered sequences from Disprot',
        'withFullyDisorder78': 'all 100% dataset + fully disordered sequences from Disprot'
    }
    
    @classmethod
    def get_info(cls, x):
        return cls.type_dataset_info[x]

class protein_seq:
    amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
                   'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']