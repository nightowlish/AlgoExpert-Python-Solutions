class DiskLevel:
    def __init__(self, disk_data):
        self.width = disk_data[0]
        self.depth = disk_data[1]
        self.height = disk_data[2]

    def can_top(self, disk):
        if self.width >= disk.width:
            return False
        if self.depth >= disk.depth:
            return False
        if self.height >= disk.height:
            return False
        return True
        
    def get_values(self):
        return [self.width, self.depth, self.height]


def getDiskTower(disks, indexes, current_index):
    tower = []
    while not current_index is None:
        tower.append(disks[current_index].get_values())
        current_index = indexes[current_index]
    return tower[::-1]

def diskStacking(disks):
    disks = [DiskLevel(disk) for disk in disks]
    disks.sort(key=lambda x: x.height)
    heights = [disk.height for disk in disks]
    indexes = [None for disk in disks]
    max_height_index = 0
    for index in range(1, len(disks)):
        current_disk = disks[index]
        for prev_index in range(index):
            prev_disk = disks[prev_index]
            if prev_disk.can_top(current_disk):
                if heights[index] < current_disk.height + heights[prev_index]:
                    heights[index] = current_disk.height + heights[prev_index]
                    indexes[index] = prev_index
        if heights[index] >= heights[max_height_index]:
            max_height_index = index
    return getDiskTower(disks, indexes, max_height_index)
