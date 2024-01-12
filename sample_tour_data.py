import random
from datetime import datetime, timedelta

from backend.crud.CRUDTour import crud_tour

from backend.crud.CRUDTourDate import crud_tour_date

from backend.util import schemas


tours = [
    {
        "tour_name": "Tour 4 đảo Nam Phú Quốc - 1 ngày",
        "destination": "143 Trần Hưng Đạo, KP 7, TT Dương Đông, H.Phú Quốc, tỉnh Kiên Giang, Vietnam",
        "duration": "1",
        "description": """Với cát trắng nguyên sơ và nước màu ngọc lam, khung cảnh của Phú Quốc thực sự là một bữa 
        tiệc cho các giác quan. Bạn sẽ đến với thiên đường Hòn Móng Tay để phơi nắng trên bãi biển xinh đẹp dưới bóng 
        mát của hàng trăm cây cọ. Sau đó, bạn sẽ được khám phá thế giới dưới nước đầy màu sắc khi lặn tại Hòm Gầm 
        Ghì. Sau bữa trưa ngon miệng được chuẩn bị bởi thuỷ thủ đoàn, bạn sẽ được cảm nhận bãi biển cát ngọc ngút 
        ngàn và lặn ống thở trong làn nước trong vắt tại điểm đến cuối cùng, đó chính là Hòn Mây Rút.<br/><br/>Chưa 
        hết đâu nhé, vì hãy sẵn sàng cho hoạt động câu cá thú vị tại Hòn Thơm. Chắc chắc bạn sẽ bị mê hoặc bởi không 
        khí biển và không gian cực "chill" tại Nam Phú Quốc đấy!""",
        "adult_price": 800000,
        "child_price": 400000
    },
    {
        "tour_name": "Tour 3 đảo VIP Nha Trang - Hòn Tằm - 1 ngày",
        "destination": "172/14/4 Bạch Đằng, Tân Lập, Thành phố Nha Trang, Khánh Hòa 650000, Vietnam",
        "duration": "1",
        "description": """Với tour này, bạn sẽ khám phá Hòn Mun hoặc Vịnh San Hô (dựa vào điều kiện thời tiết), 
        làng chài nổi trên biển, và MerPerle Hòn Tằm Resort trong nửa ngày. Bạn sẽ thấy cực kỳ phấn khích khi đặt 
        chân đến Vịnh San Hô xinh đẹp, nơi bạn sẽ được khám phá những rạn san hô nhiều màu sắc và chơi đùa với những 
        đàn cá đang tung tăng bơi lội. Để rồi đến với làng chài nổi trên biển và thưởng thức bữa trưa hải sản thịnh 
        soạn.<br/><br/>Tiếp theo, bạn sẽ tham quan MerPerle Hòn Tằm Resort, một trong những resort sang trọng nhất 
        Nha Trang. Chưa hết, bạn còn có thể tham gia các trò chơi nước như chèo thuyền kayak, đá bóng, bóng chuyền 
        bãi biển, hay đơn giản là ngắm cảnh và thư giãn. Bạn đã sẵn sàng để bắt đầu chuyến đi ngay bây giờ chưa nào?""",
        "adult_price": 750000,
        "child_price": 475000
    },
    {
        "tour_name": "Tour khám phá Bà Nà Hills (Cầu Vàng Đà Nẵng) - 1 ngày",
        "destination": "Hoà Ninh, Hòa Vang, Đà Nẵng, Vietnam",
        "duration": "1",
        "description": """Bà Nà Hills là khu phức hợp giải trí và resort lớn nhất tại Việt Nam. Cùng nhau đi tour và 
        xả láng cả ngày tại Bà Nà Hills ngay nào! Tận hưởng không khí mát lạnh cùng phong cảnh tuyệt vời, ăn hết mình 
        với đủ loại ẩm thực và chơi hết sức với những lễ hội và các hoạt động giải trí đa dạng diễn ra hằng ngày, 
        tất cả đều ngay tại đây!""",
        "adult_price": 1500000,
        "child_price": 1200000
    },
    # Bạn có thể thêm thông tin cho các tour du lịch khác ở đây
    {
        "tour_name": "Tour săn mây và đón bình minh tại Đà Lạt - Nửa ngày",
        "destination": "Đà Lạt, Lâm Đồng, Vietnam",
        "duration": "1",
        "description": """Chẳng gì có thể miêu tả được cảm giác bâng khuâng khi một người được chứng kiến thời khắc 
        bình minh "vỡ" ra trên bầu trời đầy những vệt màu tối. Bình minh đến, làm bầu trời rực sáng lên với những tia 
        nắng ấm áp và mời gọi mà nó mang theo.<br/><br/>Đã đến lúc bạn tham gia tour du lịch nửa ngày này và trải 
        nghiệm Đà Lạt ở một ánh sáng khác rồi. Chuyến tham quan sẽ đưa bạn đến những địa điểm được tìm kiếm nhiều 
        nhất ở thành phố này. Ghé thăm một nơi cực đặc biệt mà từ đó bạn có thể thấy Đà Lạt trở mình thức dậy, 
        thấy mặt trời mọc và những đám mây đang nhảy múa dưới chân, thăm những ngọn đồi chè trải dài tít tắp tại Cầu 
        Đất Farm và lạc lối trong vẻ đẹp rực rỡ của bầu không khí lạnh tan và những tán cây xanh ngắt của núi rừng 
        Tây Nguyên. """,
        "adult_price": 350000,
        "child_price": 175000
    },
    {
        "tour_name": "Tour Hoa Lư, Tràng An, và Hang Múa - 1 ngày",
        "destination": "Tràng An, Tân Thành, Tp. Ninh Bình, Ninh Bình, Vietnam",
        "duration": "1",
        "description": """Được người dân Việt Nam thân thương gọi là "Hạ Long trên cạn," Ninh Bình có thể được gọi là 
        người em gái hiền lành nhưng không kém phần quyến rũ của người chị là vịnh Hạ Long. Nổi tiếng với rừng quốc 
        gia, hang động, dòng sông yên bình và các di tích lịch sử, đã đến lúc Ninh Bình có được sự công nhận tương 
        xứng với vẻ đẹp của nơi này.<br/><br/>Chuyến thăm đầu tiên của bạn là di tích Hoa Lư. Từng là thủ đô của Việt 
        Nam, Hoa Lư mang theo một quá khứ huy hoàng và một cảm giác hoài niệm đầy chất thơ. Đạp xe qua Hoa Lư và tìm 
        hiểu về các di tích lịch sử, ghé thăm đền thờ vua Đinh Tiên Hoàng và Lê Đại Hạnh, và tận hưởng sự yên tĩnh 
        của vùng đồng quê. <br/><br/>Khám phá Quần thể danh thắng Tràng An, di sản văn hóa và thiên nhiên thế giới do 
        UNESCO công nhận. Ngồi trên thuyền và hãy nhìn lên và xung quanh bạn, bởi vì bạn sẽ được bao quanh với những 
        cánh đồng lúa tuyệt đẹp, những ngọn núi đá vôi hùng vĩ và một bầu trời xanh ngắt. Kết thúc một ngày đáng nhớ 
        với một chuyến leo bậc thang lên đỉnh Hang Múa, nơi bạn có thể có tầm nhìn 360 độ của một Tràng An hoang sơ 
        và đẹp đến nao lòng.<br/><br/>Hãy đến, và khám phá vẻ đẹp thực sự của miền Bắc Việt Nam.""",
        "adult_price": 1185000,
        "child_price": 890000
    },
    {
        "tour_name": "Tour du thuyền vịnh Hạ Long - 1 ngày",
        "destination": "Hạ Long Bay, Thành phố Hạ Long, Quảng Ninh, Vietnam",
        "duration": "1",
        "description": """Chạy trốn Hà Nội 1 ngày để đến với vùng thiên nhiên tuyệt đẹp của Vịnh Hạ Long, viên ngọc 
        quý xanh biếc một màu của Việt Nam. Tận hưởng một ngày tham quan các hòn đảo của vịnh và đánh thức tâm hồn 
        dạo chơi của bạn với nhiều hoạt động bạn sẽ khó tìm thấy được ở nơi khác.<br/><br/> Lướt qua vùng nước yên 
        bình để đến với những hòn đảo nhỏ xinh và những dốc đá vôi sừng sững, và bạn sẽ đến hang Sửng Sốt, 
        ngôi nhà của những nhũ đá với đa dạng những hình thù thật đáng sửng sốt.<br/><br/>Và nếu lên rừng xuống biển 
        không phải "nghề" của bạn, thì khoan đi vội, vì vẫn còn hiên tắm nắng trên tàu chào đón bạn, cho bạn một 
        chiếc ghế dài và một không gian để thở vào những làn gió man mát và ngắm nhìn những hòn đảo vây quanh.  """,
        "adult_price": 1000000,
        "child_price": 750000
    }
    # Thêm thông tin cho các tour du lịch còn lại
]
tours += [
    {
        "tour_name": "Tour trải nghiệm Hà Giang - 3N2Đ",
        "destination": "Hà Giang, Ha Giang, Vietnam",
        "duration": "3 days / 2 nights",
        "description": """Nếu bạn đang tìm kiếm 1 chuyến đi thật mới lạ ở Việt Nam thì sao lại không nghĩ ngay đến Hà 
        Giang nhỉ. Với cảnh đẹp thiên nhiên hùng vĩ và văn hóa độc đáo Hà Giang chắc chắn sẽ đem đến cho bạn nhiều 
        trải nghiệm thú vị đây. Tour 3 ngày này bạn sẽ đưa bạn khám phá các điểm du lịch nổi tiếng của Hà Giang như 
        Km0, Cột Cờ Lũng Cú, Quản Bạ, Yên Minh, và nhiều điểm hấp dẫn khác.<br/><br/>Chưa dừng lại ở đó, bạn còn ghé 
        thăm Công viên địa chất Cao nguyên đá Đồng Văn, được UNESCO công nhận là Công viên địa chất toàn cầu và chinh 
        phục đèo Mã Pí Lèng, một trong tứ đại đỉnh đèo của miền bắc. Và để chuyến đi thêm phần trọn vẹn bạn hãy mở 
        lòng mình để cảm nhận rõ hơn về văn hóa đặc sắc của các đồng bào dân tộc thiểu số ở Hà Giang nhé. Chuyến đi 
        này hẳn là dành cho các tâm hồn yêu thiên nhiên đây.""",
        "adult_price": 2400000,
        "child_price": 2000000
    },
    {
        "tour_name": "Đi bộ dưới biển Seawalker và khám phá 4 đảo Phú Quốc - Tour 1 ngày của Namaste",
        "destination": "Nguyễn Văn cừ, tổ 4, kp1, Phú Quốc, Kiên Giang, Vietnam",
        "duration": "1",
        "description": """Đã đến lúc bận rộn một tí và khám phá những hòn đảo xinh đẹp và thế giới hải dương lộng lẫy 
        của Phú Quốc. <br/><br/>Điểm đến đầu tiên trong ngày của bạn sẽ ở đáy biển! Với Seaworld, giờ đây khám phá 
        đại dương đã trở nên dễ dàng hơn bao giờ hết! Với công nghệ bơm khí vào nón lặn để khách có thể thở trực tiếp 
        như bình thường và với hoạt động được thiết kế không đòi hỏi khả năng biết bơi, bạn chỉ việc đi bộ dưới đáy 
        biển, ngắm và được bao quanh bởi san hô và các loài cá đầy màu sắc, còn lại cứ để Seaworld lo!<br/><br/>Sau 
        đó trở về đất liền và tiếp tục tận hưởng bầu trời nhiệt đới rực rỡ với nước biển xanh ngọc lục bảo, 
        những bãi biển giòn màu nắng và bữa trưa thịnh soạn tại hòn Gầm Ghì, hòn Móng Tay, hòn Mây Rút Trong. Còn chờ 
        gì nữa mà không lập tức trở thành phi hành gia của đại dương, và bước vào một hành trình thật khó quên!""",
        "adult_price": 2200000,
        "child_price": 1900000
    },
]

tour_dates = [
    {
        "departure_datetime": "2024-1-01",
    },
    {
        "departure_datetime": "2024-1-02",
    },
    {
        "departure_datetime": "2024-1-03",
    },
    {
        "departure_datetime": "2024-1-04",
    },
    {
        "departure_datetime": "2024-1-05",
    },
    {
        "departure_datetime": "2024-1-06",
    },
    {
        "departure_datetime": "2024-1-07",
    },
    {
        "departure_datetime": "2024-1-08",
    },
    {
        "departure_datetime": "2024-1-09",
    },
    {
        "departure_datetime": "2024-1-10",
    },
    {
        "departure_datetime": "2024-1-11",
    },
    {
        "departure_datetime": "2024-1-12",
    },
    {
        "departure_datetime": "2024-1-13",
    },
    {
        "departure_datetime": "2024-1-14",
    },
    {
        "departure_datetime": "2024-1-15",
    },
    {
        "departure_datetime": "2024-1-16",
    },
    {
        "departure_datetime": "2024-1-17",
    },
    {
        "departure_datetime": "2024-1-18",
    },
    {
        "departure_datetime": "2024-1-19",
    },
    {
        "departure_datetime": "2024-1-20",
    },
    {
        "departure_datetime": "2024-1-21",
    },
    {
        "departure_datetime": "2024-1-22",
    },
    {
        "departure_datetime": "2024-1-23",
    },
    {
        "departure_datetime": "2024-1-24",
    },
    {
        "departure_datetime": "2024-1-25",
    },
    {
        "departure_datetime": "2024-1-26",
    },
    {
        "departure_datetime": "2024-1-27",
    },
    {
        "departure_datetime": "2024-1-28",
    },
    {
        "departure_datetime": "2024-1-29",
    },
    {
        "departure_datetime": "2024-1-30",
    },
    {
        "departure_datetime": "2024-1-31",
    },
    {
        "departure_datetime": "2024-2-01",
    },
    {
        "departure_datetime": "2024-2-02",
    },
    {
        "departure_datetime": "2024-2-03",
    },
    {
        "departure_datetime": "2024-2-04",
    },
    {
        "departure_datetime": "2024-2-05",
    },
    {
        "departure_datetime": "2024-2-06",
    },
]


for tour in tours:
    tour["duration"] = int(tour["duration"][0])
    # print(tour)
    # tour_insert= schemas.TourCreate(tour)
    # tour_insert= schemas.TourCreate(tour_name=tour["tour_name"], destination=tour["destination"], duration=tour["duration"], description=tour["description"], adult_price=tour["adult_price"], child_price=tour["child_price"])
    # tour_insert.tour_name = tour["tour_name"]
    # tour_insert.destination = tour["destination"]
    # tour_insert.duration = tour["duration"]
    # tour_insert.description = tour["description"]
    # tour_insert.adult_price = tour["adult_price"]
    # tour_insert.child_price = tour["child_price"]
    # print(tour_insert)
    tour["name"] = tour["tour_name"]
    del tour["tour_name"]
    tour_insert = schemas.TourCreate(**tour)
    crud_tour_insert = crud_tour.create_tour(tour=tour_insert)

    for date in tour_dates:
        date["tour_id"] = crud_tour_insert.id

        # date["return_datetime"] = datetime.datetime.strptime(date["departure_datetime"], "") + datetime.timedelta(
        #     days=tour_insert.duration)
        # date["return_datetime"] = datetime.datetime.strptime(date["departure_datetime"], "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
        #     days=tour_insert.duration)
        # print(type(date["departure_datetime"]))
        # date["departure_datetime"] = datetime.strptime(date["departure_datetime"], "%Y-%m-%d %H:%M:%S")
        date["departure_datetime"] = datetime.date(datetime.now()) + timedelta(days=random.randint(1, 50))
        # date["departure_datetime"]= date["departure_datetime"]

        date["return_datetime"] = date["departure_datetime"] + timedelta(days=tour_insert.duration-1)
        # print(date)
        # date_insert = schemas.TourDateCreate(tour_id=date["tour_id"], departure_datetime=date["departure_datetime"], return_datetime=date["return_datetime"])
        date_insert = schemas.TourDateCreate(**date)
        crud_tour_date.create_tour_date(tour_date=date_insert)
