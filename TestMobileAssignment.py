
from Phone import mobile
from Phone.mobile import Iphone, Micromax, Samsung



def listofmobiles():

    #price,specifications,vendor,IsDiscount---Pass this parameters
    samsungEdge = Samsung(45000,{'Color':'Black','RAM':'4GB','Camera':'13MP'},'Samsung',0.10)
    iphone = Iphone(95000, {'Color': 'Silver', 'RAM': '6GB', 'Camera': '14MP'}, 'Iphone', 0.15)
    mi = Micromax(25000,{'Color': 'Silver', 'RAM': '6GB', 'Camera': '15MP'}, 'MI')

    samsungCurve = Samsung(45000, {'Color': 'Black', 'RAM': '6GB', 'Camera': '16MP'}, 'Samsung', 0.10)
    iphonex = Iphone(99000, {'Color': 'Silver', 'RAM': '8GB', 'Camera': '17MP'}, 'Iphone', 0.15)
    mix = Micromax(35000, {'Color': 'white', 'RAM': '9GB', 'Camera': '18MP'}, 'MI')
    return[samsungEdge,iphone,mi,samsungCurve,iphonex,mix]

SamsungTotalPrice = 0.00
IphoneTotalPrice = 0.00
MixTotalPrice = 0.00

SamsungTotalDiscount = 0.00
IphoneTotalDiscount = 0.00
MixTotalDiscount = 0.00

def main():

    Mobile_list = listofmobiles()

    if mobile.Mobile_vendor.lower() == 'Samsung'.lower():
        SamsungTotalPrice += price
        SamsungTotalDiscount += IsDiscount

        print('Samsung Total Price',SamsungTotalPrice)
        print('Samsung Total Discount',SamsungTotalDiscount)

    elif mobile.mobile_vendor.lower() == 'IPHONE'.lower():
        IphoneTotalPrice += price
        IphoneTotalDiscount += IsDiscount

        print('Iphone Total Price', IphoneTotalPrice)
        print('Iphone Total Discount', IphoneTotalDiscount)

    elif mobile.mobile_vendor.lower() == 'MI'.lower():
        IphoneTotalPrice += price
        IphoneTotalDiscount += IsDiscount

        print('MI Total Price', MITotalPrice)
        print('MI Total Discount', MITotalDiscount)
    else:
        raise 'Enterd Mobile is Invalid'

if __name__ == '__main__':
    main()