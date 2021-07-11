# Pi number bar chart animation generator.
# Copyright (C) 2021  RazerMoon
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

nums = [0] * 10
strpi = str(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)

def barlist(n):
    nums[int(strpi[n])] += 1
    return nums

fig = plt.figure()

dig_text = plt.text(8.5, -1.5, "1/100")

barcollection = plt.bar(range(0, 10), nums)


def init():
    plt.ylim(bottom=0, top=15)
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.title("Digits of Pi")
    pass


def animate(i):
    dig_text.set_text(f'{i+1}/100 Digits')
    y = barlist(i)
    for i, b in enumerate(barcollection):
        b.set_height(y[i])


anim = FuncAnimation(fig, animate, repeat=False,
                     init_func=init, blit=False, frames=100, interval=100)


anim.save('100_digits_of_pi.gif', writer='ffmpeg')
