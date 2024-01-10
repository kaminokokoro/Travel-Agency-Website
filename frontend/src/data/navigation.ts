import { NavItemType } from "shared/Navigation/NavigationItem";
import ncNanoId from "utils/ncNanoId";


export const NAVIGATION_DEMO: NavItemType[] = [
  {
    id: ncNanoId(),
    href: "/listing-stay-hanoi",
    name: "Khách sạn",
  },
  {
    id: ncNanoId(),
    href: "/listing-experiences",
    name: "Tours",
  },
  {
    id: ncNanoId(),
    href: "/listing-flights",
    name: "Chuyến bay",
  },
];
