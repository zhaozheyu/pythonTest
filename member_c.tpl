<?xml version="1.0" encoding="utf-8"?>
<card flex-direction="column" width="100%" height="230" onTouch="">
    <view flex-direction="row" width="100%" height="40"  align-items="center" padding-left="16">
        <label maxLines="1" text="{{ .text0}}" textColor="#666666" textSize="12" margin-right="5" textStyle="bold"/>
        <image url="{{ .image0}}" width="15" height="10" margin-left="3" />
        <view width="2px" height="9" backgroundColor="#d9d9d9" margin-right="10" margin-left="10"/>
        <label maxLines="1" text="{{ .text1}}" textColor="#666666" textSize="12"/>
    </view>
    <view flex-direction="column" width="100%" height="130" onTouch="sdf">
        <image url="{{ .image2}}" position="absolute" width="100%" height="100%"/>
        <label highlightTextColor="#ff0000" highlightTextSize="18" text="{{ .text2}}" maxLines="1" margin-top="14" textColor="#ffffff" textSize="14" margin-left="16"/>

        <view flex-direction="column" width="100%"  top="76" position="absolute" padding-left="16" padding-right="16">
            <view  backgroundColor="#33ffffff"  cornerRadius="2px" height="4px" width="100%"  />
        </view>
        <view flex-direction="column" width="100%"  top="76" position="absolute" padding-left="16" padding-right="16">
            <view  backgroundColor="#ffffff"  cornerRadius="2px" height="4px"  width="10%"/>
        </view>
        <view flex-direction="row-reverse" align-items="center" margin-top="78"  padding-right="16" position="absolute" padding-left="16" height="52" width="100%" onTouch="{{ .link0}}">
            <image url="http://img-ys011.didistatic.com/static/xpanel/oc_vip_card_white_arrow.png" width="6" height="10" />
            <label text="{{ .text4}}"  flex-grow="1" textSize="14" textColor="#ffffff"/>
        </view>
    </view>
    <view flex-direction="row" width="100%" margin-top="6" height="50">
        <view x-for="{{.buttons}}" align-items="center" flex-direction="column" onTouch="{{ .item.link}}" width="20%">
            <view width="35%" position="absolute" right="0">
                <view backgroundColor="#ff0000" cornerRadius="2" width="4"  height="4"/>
            </view>
            <image width="20" height="20" url="{{.item.image}}"/>
            <label margin-top="4" text="{{.item.text}}" textColor="#666666" textSize="12" textAlignment="center" />
        </view>
    </view>
</card>
