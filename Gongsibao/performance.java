/**
         * get the current page loading time ,it will return seconds
         * @param driver
         * 
         * @see http://www.softwareishard.com/blog/firebug/support-for-performance-timing-in-firebug/
         * @see http://selenium.polteq.com/en/implement-web-timings/
         * @see http://www.html5rocks.com/en/tutorials/webperformance/basics/
         * @see http://www.theautomatedtester.co.uk/blog/2010/selenium-webtimings-api.html
         */
        public long getPageLoadTime(){
            long pageloadtime=0;
            long pagestarttime=0;
            long pageendtime=0;
            
            //try{
            //different with browser ,ie will return is double value but firefox and chrome will return is long
            Object startobject=executeJSReturn("return window.performance.timing.navigationStart;");
            Object endobject=executeJSReturn("return window.performance.timing.loadEventEnd;");
            //@SuppressWarnings("unchecked")
            // pagetimer=executeJSReturn("var performance = window.performance || window.webkitPerformance || window.mozPerformance || window.msPerformance || {};"+
              //             " var timings = performance.timing || {};"+
                //           " return timings;");
            //long pageloadend=(pagetimer.get("loadEventEnd"))/1000;
           //    long pageloadstart=(pagetimer.get("navigationStart"))/1000;
            //pageloadtime=(pageloadend-pageloadstart);
            //think it's the firefox or chrome browser
            if(startobject instanceof Long){
                pagestarttime=(Long) startobject;
                logger.debug("the page navigate start time is:"+pagestarttime);
            }
            if(startobject instanceof Double){
                Double tempvalue=(Double) startobject;
                pagestarttime=new Double(tempvalue).longValue();
                logger.debug("the page navigate start time is:"+pagestarttime);
            }
            if(endobject instanceof Long){
                pageendtime=((Long) endobject);
                logger.debug("the page end time is:"+pageendtime);
            }
            if(endobject instanceof Double){
                double tempvalue=(Double) endobject;
                pageendtime=new Double(tempvalue).longValue();
                logger.debug("the page end time is:"+pageendtime);
            }
            
            pageloadtime=(pageendtime-pagestarttime)/1000;
            logger.info("Get current page loading time is:"+pageloadtime);
        
            return pageloadtime;
        }