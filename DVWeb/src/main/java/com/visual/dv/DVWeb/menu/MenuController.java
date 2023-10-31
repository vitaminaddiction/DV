package com.visual.dv.DVWeb.menu;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("menu")
public class MenuController {

    @GetMapping("menu1")
    public String menu1(){
        return "menu/menu1";
    }

    @GetMapping("menu2")
    public String menu2(){
        return "menu/menu2";
    }

    @GetMapping("menu3")
    public String menu3(){
        return "menu/menu3";
    }

    @GetMapping("menu4")
    public String menu4(){
        return "menu/menu4";
    }

}
