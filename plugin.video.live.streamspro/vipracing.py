import math
import urllib, urllib2
import re
def vip_unlockmeta(meta):
	d=''
	for i in range(0, len(meta)):
		if (i % 3 == 0):
			d += "%";
		else:
			d += meta[i];
	return urllib.unquote(d);

def get_html(meta,data):
	meta_un=vip_unlockmeta(meta)
#	print meta_un;
#	return 
	oo=''
	x=data
	l = len(x)
	b = 1024.0
	i, j, r, p = 0,0,0,0
	s = 0
	w = 0
	str_pattern='Array\((.*?)\)'
	array_val=re.compile(str_pattern).findall(meta_un)[0] 
	t_string = 't=['+array_val+']'
	exec(t_string)
#	print t_string
#	return
	#print math.ceil(l / b)
	#print t
	for j in range(int(math.ceil(l / b)), 0, -1):
		r = '';
#		for (i = ath.min(l, b); i > 0; i--, l--):
		for i in range( int(min(l, b)),0, -1):
#			w |= (t[ ord(x[p]) - 48]) << s;
#			print i-1024, p
			w |= (t[ ord(x[p]) - 48]) << s;
			p+=1;
			if (s):
				r += chr(165 ^ w & 255);
				w >>= 8;
				s -= 2
			else:
				s = 6
			l-=1
		oo += r
	return oo

def getUrl(url, cookieJar=None,post=None, timeout=20, headers=None):
	cookie_handler = urllib2.HTTPCookieProcessor(cookieJar)
	opener = urllib2.build_opener(cookie_handler, urllib2.HTTPBasicAuthHandler(), urllib2.HTTPHandler())
	#opener = urllib2.install_opener(opener)
	req = urllib2.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
	if headers:
		for h,hv in headers:
			req.add_header(h,hv)

	response = opener.open(req,post,timeout=timeout)
	link=response.read()
	response.close()
	return link;

def decrypt_vipracing(page_url, justHtml=False,doDecrypt=True):
	page_data=getUrl(page_url);
	url=page_url
	if doDecrypt:
		str_pattern='src="(.*?(\/embed).*?)"'
		url=re.compile(str_pattern).findall(page_data)[0][0]
		#print url
		meta,data='',''
		headers=[('Referer',page_url)]
		html=getUrl(url,headers=headers)
		
		str_pattern='\'(http.*?)\''
		url=re.compile(str_pattern).findall(html)[0]
		html=getUrl(url,headers=headers)
		
		
		str_pattern='c=\"(.*?)\"'
		meta=re.compile(str_pattern).findall(html)
		if len(meta)>0 and len(meta[0])>0:
			meta=meta[0]
			str_pattern='x\(\"(.*?)\"\)'
			data=re.compile(str_pattern).findall(html)[0] 
			#meta="x66p75X6eE63S74j69x6fR6eC20k78r28J78v29r7bu76V61O72I20Q6ct3de78T2eh6cI65O6eZ67b74y68l2cD62e3d@31Z30Z32Z34t2cG69b2cU6af2cc72N2cd70e3dk30K2c_73h3dK30u2cr77M3dw30n2cB74M3dN41p72r72_61a79L28H36j33N2cF34n32N2cW31_35x2cC35K33e2cQ35f34H2ci31F34r2ct34I31b2cj32E39P2cH38z2cQ31B36Y2cR30R2cV30o2cJ30d2cj30n2cz30p2ca30R2c_39e2cI31q31F2cc31q2cj35U35D2cm33R38h2cN31i37_2cx34D35E2cR35T2cf35f32o2cA34h36M2cb33_32_2cs32v35a2ci32T37k2cW32U36g2cA34W37a2cu36V32s2ch32B34P2cB33v30G2cm33Q2c_33n37L2cR37Y2cW34t30J2cW32X38F2cs33J39v2cj35T37U2cw36A31Q2cZ35j39Z2cQ30D2ck30A2cG30_2cD30M2cE33K31@2cI30M2cL31M38h2cM35r31u2cy30E2cH34u2cT32q30J2ch33r34l2cV31e32d2cM31u39n2ch36C2cO33z36e2cI36p30U2cX32E2cf32y33V2cU34M33b2cs35b38J2cX31x30G2cv32u31d2cr33k33K2cD34T34G2cD35C30C2cG32H32_2cX34V39t2ce34L38t2cx33R35f2cm31K33P2cs35k36S29M3bg66a6fz72_28a6aW3da4do61d74o68d2eK63E65n69e6cb28o6cq2ff62C29M3bX6ag3el30Z3bh6an2dv2dN29Q7bC72Q3dw27z27f3bs66y6fL72@28_69K3dN4dh61C74S68Y2ed6dQ69D6eY28n6cs2ct62Y29H3bi69T3ez30w3ba69_2dw2dF2cy6cx2dP2dX29Z7bZ77z7cw3dC28y74Y5bs78r2eY63r68y61L72Y43l6fh64g65f41J74B28u70e2bX2bi29g2dQ34B38l5dJ29U3cZ3cS73g3bi69g66z28q73Q29o7bZ72A2bq3di53S74E72j69s6eK67b2eI66O72C6fC6dF43A68_61N72j43u6fJ64s65v28O31c36o35W5en77_26P32V35@35V29U3bo77U3eu3ek3dg38D3bj73_2d_3dI32v7dG65u6cS73x65r7bC73W3dr36T7dT7dl64e6fe63_75q6df65J6eg74Q2eX77Y72B69n74t65_28E72B29m7d@7d";
			#data="ND@r8f8XB_VtpLsbqWgHumPwcTywiTFtmm8vATVrTWstiZVr8fzDND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTuU3mLgDT1zbun8vB2ywmTybuRgtcNVHAOs3TIKDpMFvmbV3ENXnND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTIXnstkwG4PwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrERs3ERk3TtPrdfKr9NVwc2gbARVwgOpnQ0pnGuPrGistiRytcNVHApY3gTywypUJgoXnsfYnslVtuRknsoYnsistiRytcNVHApY3gTywypPDg2k3dxgwGMY3ixKOT18b8hswcLFfdTs3TWstiZgwmNP3AAVOTuUHgTVHyxKOT5KSqD0rG4gwgAVbExKOTiKSqD0rLD6fg2k3dxgwLp8xQOpnP0MDpMFvmbV3ENXnND@rrnIXvb_YJmPbExVtGu2kWW5ZDmzr81UftL6Xp1PzvTQrYCQkUWQreIPSGi03dNs3gTybpNgv@nUfJNOrGQPbET73_1UfaAFHApFSA1k3lnPkCnPCyTyt@h6frT_zp47bExVtefPHmhktubVHgnktdWkfBT7wTIXnK4VH8WVr7xVtALyDT4VHEmYWp1UHaAYfaLXfp_Fwpa@WVt6f7CVH8WkrG4yt@0KtdNswPQ8wAxUwT_Pr@hktlxXrcNgfl_krGIXnK4gwdTkDNuPrKfgwEhVryT7Hqx8weRybhxXrinktERktExPHVmywTuUvpNVHcNVHPQPHcC7Hp4VH8WsWGMVbd_F3cTyD9TYw84XrG1zDNuPrKiybEWgwLl5tTRVwGu7tdbywmW6fEbVH@RkDNuPrKfgwEhVrAhgtcxXr5RgCank3BLYrGMstATywATyDTpyvELVbGDgbhRVriCgvANgw@L7fGDgbhRVfGMVbdNktcWVfGM7HmRgv8bktlWPrT_FtdTsvdL7H@u8t9LybiWPrhbVwcns3@uU3qnk3EWPrERVtc2ybubstAWPr8nkHgRs3@uzwpnVHThVt@WPrunsviRk3@uP3@hgCc_YrG1zDNuPrKfgwEhVrAhgtcxXrBRs3i_ybqTybpNkrGMstATywATyDTtQtg2ywAiFtGl5tTRVwGu_tdbywm_PrpIXnsD63i_ybqTYDNtpng2VryiFtqNPtpLgvEbstAm8DPuU3cWkwADstihVHgnktguUCNtpns1UfEnV3ADstihVHgnktGfKrT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nzHgRsHpaKSppyvELVb8DgbhRgfJL_YnmPzcmFtmTywuxUvyhktARVt85stmxzwmRgwToXnstp4NtMDpMFvmbV3ENXnsD63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTuU3mLgDT4VHEmYWp18v2hVCApstpAVtchV3gLYfingtpakbdCFf@bkvunzbeRywmbFfeIPjAQ6f2hyHc_yCAfgbANzbu_zDK1U3i_ybqTYDGOMDp4gwdTkDNDXvpTgCG1ktDnktERVCEx5wARyDTQywERY3AmzwdWs3cZXrG1kt4RVtcLVH4TyvmTyDTQywERY3AmzwdWs3cZXrG1ktr_yvlL_Hd_7HPQz3cTyHmNVrRhVtuRsWTuUtALItqbyDTQywERY3AmzwdWs3cZXrG1ktDR7HPQz3cTyHmNVrRhVtuRsWTuU3Eb7tcxXr8hk3lbkt_u6WqhVwBbktl0KSTIXnKigbhmU3Eb7tcxXrqns3gTybpNkWmRVtdTybhRsWERVCEx8v@bswA06vcNVHc_FWabVwECkWhl6SqCFWyRgblCVH_i@Squ7CQQgviZswmngHATkWiuKSqoXrLOpnKigbhm8bBxXrdTsOp2ywmWgvV_PruTyC@RgDTpybBT7b_5@juu7CQ4gwgAVbE0KjeuK37ZK3pLybEbstA0@vTLFt@R7HcZKHpmYWqu7CQQzDNtpnKigbhm8bBxXrdTsOp2ywmWgvVnNvpRYtETstaNkrGM7HVWgwPQUHgTVHy0Xj9MK37ZK3pLybEbstA0@vTLFt@R7HcZKHpmYWhlK37ZKSqCFWERVCEx8v@bswA06vcNVHc_FWinVtp_YWi5kwRZXwpNVH8Myb_RkWeaK37ZXC8tktBRVC_a6WBbs3qWgvV0XtpNgwQQzDDWstuRVrdTs3GtktGD63qhktGtVwPQUvpRYtETstaNkt9xkrLD6fumyvANKruRsvpNVwuNPDpigbhNXnstMDBbkHGtVwPQ8vBnNthRk3@hgCoLstATywATYrGM7HVWgwPQzC8tktBRVC_a6WabVwECkWuuKSqCFWyRgblCVH_Q@jqu7CQuFtubVHgnkt_akvunVt9TywQiFtq0KWqu7CQDgwRTYWepXjqCFWThsv5Ak3pRYtB06rR2kwQQzDKtkwmhgtcm8bBxXrp2ywmWgvVn2bR_yv8RkrG5k3dxgwTnk3BRk3PpPSlu8td_FwgNVbcbswyTyDlu6JGfgvmAgbAAybBT7bPpPSluU3i_Ft@WgbAAgDlIstluUHgTVHyx6JuuKSluPbcbswyTyDlQ@jqpzDK18bR_yv8RkDK1Pwg2YDNtpnKigbhm8bBxXriWstuRsOTR7HEnktTuU3Eb7tcxXr_x8bATgw70XSQuFtubVHgnkt_akvunVt9TywQiFtq0KWuu7CQQyblCVH_M6Sau7CQQstmTgwm0KSTIKDdm8bBxXrdTsOp2ywmWgvVnNv@ns3c_Pry_ywRxXr2hkHdLFvmbV3E0XHpbVwyu@xTuUtALVtgLsbPQUrTIKDgxswGpgv@Wgwmbyb8AgDAnVrGMY3ixXryT7Hq06fppFHaNPwg_ywiTYSahVHiCkfingtptgtdAgwunUv@ns3cn0v9T7HpNkfqNswTu8v@TyDT4YrG1zDK18vLD6fBbkHLOpnsDKwg27rgTgDTaVwonkHc_7tdbFOinktERktEhXrGM7HVWgwPQzC8tktBRVC_M6WabVwECkWuuKSqCFWyRgblCVH_Q@jqu7CQuFtubVHgnkt_akvunVt9TywQiFtq0@juu7CQDgwRTYWepXjqCFWThsv5Ak3pRYtB0KHmhktumyvmRktEZ6tqhsvgTyC_uXfqa6WTIKDg2k3dxgwGtVwPQUthRk3@hgCobkwmhgtcn2STuzwmhgtc_stmTgwmx6JqpPr8hk3lbktyRgblCVHPpPSlu8td_FwgNsHgTVHyx6JqpPruLk3pWVtgNswPpztpAPrabVwECgDlMKSqpPryRgblCVHPpzS9u6JLD6fg2k3dxgwLD6fBbkHLOonstonsD6fBbkHLOpnKigbhm8bBxXr@bsbcnNthRk3@hgCTuU3Eb7tcxXrThsv5Ak3pRYtB06rJL5zJ25jQQstmTgwm0@SqC7runVtgTVripKj7QOX7oKbcbswyTYWeuKSqCFWabVwECkWuMKSqCFWqhVwBbktl0@jqCFWqns3gTybpNkWd_s3pWgHERsW_x8bATgw70@SQiFtq0@SquK37ZKtc2VH_a@jhI8jqCFWBbs3qWgvV0XtpNgwTIXnstMDg2k3dxgwGtVwPpPtgZgwobkwmhgtcAPrR_yv8Rkvp_7wc_yDlu6JGfgvmAgbACgwgAVbEx6JqpPr8hk3lbktabVwECgDlu6JGMFvmnVt@bktlx6JAnsJGpybBT7bPpUSuuK37APryRgblCVHPp8Squ6JGM7HVWgwPQzvp_7wc_YWGaK37mU3pWgbBmUr7i5XqMOjQQzDK18bR_yv8RkDNtpnKaVry_ywRxXr2hkHdLFvmbV3E0XHpbVwyu@xTuUtALVtgLsbPQz3cxsthRVogZgwytzrLD@b8AVrlhVt@Rk3VbgtlxXtpmPruTyC@RgDTuFtubVHgnkt_akvunVt9TywQiFtq06SqCFWmbswyTYWuu7CQQstmTgwm0KSQOyfgNVwcCYWeuKSqQPru_FvPQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfgxgvlRs3pMVtpLywo_gHETFtANP3AAkrGaVtExXr7_PrpIKDpakDNtMDpigbhNXnsDKwg27rgTgDTaVwo2stpTywm_PruTyC@RgDTpybBT7b_aKSqlUWyRgblCVH_tKSqCFWqns3gTybpNkWd_s3pWgHERsW_x8bATgw70@SQQstETFt80XShu7CQDgwRTYWqoKwgL73@hgC_IstARkrLOpnsDKwg27rgTgDTaVwo2stpTywmnNvpNVHcNVHTuU3Eb7tcxXrqns3gTybpNkWd_s3pWgHERsWabVwECkWeuKScoKbcbswyTYWeuKScoXrLD@bR_yv8RVrgTgDl5stpTywmn2bR_yv8RsJG5k3dxgwTnk3BRk3PpPSlu8td_FwgNVbcbswyTyDlu6JGfgvmAgbAAybBT7bPpPSluU3i_Ft@WgbAAgDlIstluUHgTVHyx6JeuKScpPryRgblCVHPp8Squ@JlIKDptkwmhgtcNKDpigbhNXnstMDdmPbmRkwPQzbd2yvuLk3gm7H_5FtgTVxqtzrG1ktiWgbiZgDTQyw8nkHc2ItpTywmCQkUWQxgQzDKtgtlmUwdWVtc_yCgxswPIstGuU3Eb7tcxXrqns3gTybpNkWd_s3pWgHERsWEnV3_MK37ZX3gAVbE06SqCFWTnk3BRk3_u6W_x8bATgw70@SquKSTuU3mLgDT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8n8b8hswcLFfiWstuRsOTR7HEnktAuYtl_PrdWVHPQPCTuUfLD6fdNXnsD6fBbkHLOonsDKwg27rgTgDTiV3@hgCc_YrGM7HVWgwPQUHgTVHy0Xj9MK37ZKbcbswyTYWEaKSqCYrQOyfgNVwcCYWeoXDK1Pwg2YDNOpnKMFvmbV3EmPwdTyv8MkwdLyCALgDT5gv@LywTuPHVmywPQPHcC7HpOgvhhs3i_ybqTYrGMY3ixXryT7Hq06fpakbdCYflnstlWgwdmybuNUvpxsfd0gv7nPtg_s3pOg39Rk3Vn8SApXfm1zbeRywmbYf8bktAOs3TIKDpMFvmbV3ENXnsD63i_ybqT7rBhVHdxUvRhs3VNsvPQzwdWs3c_PrEb73cx6JERVCEnzbd2yvuLk3gm7HluU3mLgDl4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nP3@hgCc_FfqWgvVRk38lXfhIzbuAzDK1U3i_ybqTYDNOpnKMFvmbV3EmPHVmywPQPHcC7HpOgvhhs3i_ybqTYrLOoHd_7rEnsbcNVrPuzrToXnBIUwcTYZ4nOoyQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfuRk3hRk3Au7bqn@bBx@SEa@jeuKSEM@jTDPrRRYtiTybpNVx2LFtAbUCNtMHpZgwAm8DGOs3pNkfEnsbcNsWNt13cTFYE_ywdxVxEnsbcNgxQOp4goXnN5gHALVHgnktGMywEL_HmRgv8CPHpZgwAbPrQ0pnGuzbam7tdbywmCUJBm7tdbywmA8xAMywER73yoYnst1JgTsJ_uUJBm7tdbywmAPfNtpnlagHEns3Ehk3EAzWGpPHmRywlDznst1JabVwECsJ_uUJhl6SlDznst1JyRgblCVHlOKrli@SqpPfNtpnlMstATY3pWkvd_FJ_pzvpT7HpxsJ@OpnspP3mnkHgTgwmAzWGpz3ExV3lDznst1JmTytqNPH9NktcWgbAAsJ_5gv@Lyw@OMrst1JTRYwRRk36RktlT7blOKSAaKfNtpnlM7HmRgv8Rk3lOKrTQ7H8mYWXnPOppyvELVbeIPwg_ywiTYSahVHiCkfingt_a@WulKOpigbmRsvE_6HdTFvyWNfoTgwRbktuTFOXnUD7LyDoAywoTgtyT6ov02jk_KHELszxT6vFR5SRT5zqfQkwCyorhNHU0Yk71QzsRYorR2HUT2kVWObk_XwrR_SnT_bgnQzJ0FovLkCUTO071QkbWg02LsHUA5o_xIzsCy0vN5bk0Yk@NOCJTXorCkb1A2oqfObi_@orRISUT2z7NIkNbkojNzfTDznstMrEnsbcNkWGiFt5Rkt@OpnspzwgWgwlOKrl57b7bXjVLsb8myv7my39Izw@2FJ@Opnsp8tpTgwuAzWGo0nstpnQTyCqRkWGpzw@hs3yAPfGMY3i0Krl4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nP3@hgCc_FfqWgvVRk3oRgtTRVwobsw9bVwcNU3a2sJPWznstpnQ0pnstMrGiyCqRkWGpPbExVt9pPfNtpnsuPrinktRbsw_uUCNtpnsuPrGpzwgWgwlOKrl4VHEmYWp18tp_gb@Rs3E_ywdxgbAAkfgWgbhRkfEnkWet6S918wBAgwp57b7bXjVLsb8myv7my391P3@hgCqWgbuTYf8L@H7pPfNtpnsuPrGpP3mnkHgTgwmAzWGpzHgTgwpAznstpnGu84NtpnsfYnstpONtMrGfyxQOp4NtMDpMFvmbV3ENXnsD6fBbkHLOMDuLk3gm7HLO1vBbOtERk3hhVtPIgH@WsWNQyw@ngvBm8DG5gv@LywQOow9NsvEbstAmPtgZgwDWgbiZgwBC8xGoYnsistiRytcNVHApgwERQtcxgwATYXVbQwyQPtgZgwonkHc_7tdbYrgIU3Eb7tcNPwgL73@hgCPQzv@nsv5_UWstpnstpnNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzr@bsbcn2bR_yv8RkrgIU3mLgDT4VHEmYWp1UHaAYfRhsvc_stpZkfingtpu7t9AgbALFf@bsbcNP3ymFDy_ywRxKbET73cM@XcQXzcQXzaAFHA5gviRkvpnsbAMst8RzSxbVtg2ywAiFtRMywATgDRhVtuRkJ@hgCpR7HPM7HdNVwd_7wRpybBT7bPMXSq5U3ynsHo2gviRs3P5gv@LywRasvEbstAxKtgZgwRMst@nk3uLVbcxgwPDgblCVHR5stATYJyRgblCVHP4@jToXnP0ow9NsvEbstAmz3cxsthRVogZgwytPrQ0pnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTDgb5RsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTIstARkrQOp4N5gHALVHgnktGMVtgLsb6bs3ERktc_7xguUCNt1HgNVwpAYfpmywACzryT7Hq06fppFHaN8tV2gviTYfE2FfcWgfiWgvubsvpxzvd_FvcWstAhgfhLyfmRgv@x8tdNVwmbVwpQ8xQOp4N5gHALVHgnktG1V3cNsXyhktARVtytPrQ0pnabktBnsHA1V3cNVxT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8nzHgRsHpaKSppyvELVb8DgbhRgfJL_YnmPzcmFtmTywuxUvyhktARVt85stmxzwmRgwTtUWNfYnRRYtiTybpNVrmRgtp2yw12ywmWgvVCQkUWQxgO1CNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTIstARkrQOpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxT1kHc_7tdbFOg2k3dxgwTtzfu_FvPQzrQOpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTaVwonkHc_7tdbFOiWstuRkrgIU3Eb7tcNPwgL73@hgCPQztpNgwToXnsMVtchk3sNVHc_YHdWVxiTgZATywm2yv@bUWNt13cT7kgxgwpR7HypU3cTFohRk3@hgCFT2o6C8xlDPr7iKSquKSgoXnsQyw@ngvBm8DGiY39RsWNfYnRRYtiTybpNVrECgbuxIthbgwyfsthbgwnhgtcbPrQ0pnGtkwG4ztd2yblhVHp_Yfdm73nhgtcN8bATgw7nOwyQ8ogLk3pLFtRTYrgu8rPu8fetPrQ0pnsuz3cTyHmNVrabktBnsHAistiRytcNVHOxsthbgwnhgtcxNWNtMrPm8w@LywGoYnstMrmRVH9_YtGistiRytcNVHApgwERQtcxgwATYXVbQwyfsthbgwnhgtcbUWNtMrP0MrP0ow9NsvEbstAmU3cTFohRk3@hgCFT2o6C8xNoYnstpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxT1kHc_7tdbFOg2k3dxgwTtzfu_FvGfKrT4VHEmYWp1UHaAYfBbk3cLVHmpyvELVbAMst8n8vBLFfuuKS7_@jqIPbExVtToXnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrp2ywmWgvVn2bR_yv8RsOeQ8xAMY3im8DGQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfdTs3pMKSq4YS9uXfyTyt@_UWNtpnBnsv9xgwATYflRVHJWgw8RktE_5CsTVxTMst9NVHBnsHANgH8_8xAtktARk3FT2o6xXrhuXrQOpnsMVwsNVHc_YHdWgDuRVHsNVHc_YHdWVxTMst9NVHrnsHAC8xTD8SquKSgoXnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsOp2ywmWgvV_8xAM7HVWgwAigbum7tdbyDTQVtpLsbToXnstpnstkwG48rmRVtphVwguPHybs3UnkHgRVxTiV3@hgCc_YrgIPtcTF3qWgvVC8SgoXnstp4NOonRRYtiTybpNVruRVHxnstERk3FT2o6C8xNoYnstMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrRnstERk3obkwmhgtc_8xAMY3im8DGQPbET73_1UfaAFHAigbmRsvE_6HdTFvyNUvpxsfdTs3ppXS74yWqIPbExVtToXnsistiRytcNVHApgwERQtcxgwATYXVbQwyQ8vBn0wpnVHc_YrgIU3Eb7tcNPwgL73@hgCPQzv@nsv5_UWNtp4N5gHALVHgnktGQyw8nkHc2ItpTywmCQkUWQxgO1CNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrdTsORnstERk3TtzfuTyC@RkfBbs3qWgvVxXrAnktc_UWNtMwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzrRnstERk3obkwmhgtc_8xAMY3im8DGQzrQOp4N5gHALVHgnktGMst9NVHrnsHAC8xNoYnsMgHm_ywATFXrxK3d_F3cbOtECPwpLgH8RktENUwcTyz@RgtcNVHWbyZBCzringHAT7wpAYtARytTtzfgNktc_7ZvxQogoXnstkwG4Uv9_Y3cNVHDT5DPa@xGistiRytcNVHApgwERQtcxgwATYXVbQwyQ8vBnNthRk3@hgCoLVtpLywTtzfuTyC@RkfBbs3qWgvVxXrTWstiZkrQOpng2VryMgHm_ywATFXrx@Detznsto3cxsthRsohRk3@hgCFT2o6C8xQOpncWs3c0pnsistiRytcNVHApgwERQtcxgwATYXVbQwyQUvpRYtETstaNkt9xkrgI8bANgwmCQkUW5DyMgHm_ywATFXrx8SgoXnP0onRRYtiTybpNVr1mywAA2bATstaC8HmWVfGIgv8RVfGpybBT7b@uPbcbswyT7fGts3CRs3g0ywj_VtcbznQ0pnhhk3GDgwRT7rPu8odT7bAQFt9NVwy4U3i_ywcNkfabVwECVr8uUHgTVHybPrpuzSgoXns5yvmmPHpm7rPu8odT7bAQFt9NVwy4U3i_ywcNkfyRgblCVHGfPryRgblCVHguUfGQ@xQOpnhhk3GM7HVWgw4TY3GfKrliFtpWkvd_yDAnVf@nsvdTybpNgDAnVfBbk3cLVHp_ybcLyDAnVfuTyvERF3PIst@fgwARYvd_yDAnVfuLk3pWVtThk3uxXtpAUWNtpnuTyC@RsYE_7r5fKrlDz3cLyb_hkv@RgDluUxG48bu_2wubkCchOv@RVrMuUJVRs3luzWGpztpA8xQOpnsM7HVWgw4TY3Go8DGpPfabVwECgDluUxGpybBT7bGoPrlDPbcbswyTyDluUxG4gwgAVbEZXnst13Eb7tcL_HmmUxPuUJ@DgwRTyDluUxGDgwRT7r5uUJ@iFtqx6JGoPrEnV3QOpnsM7HVWgw4TY3Go8DGpPfuLk3cRktYx6JGoPr@RkwEmUxGpPfuLk3cRktkx6JGoPrEnV3QOpnabktBnsHA1V3cNVx9_7t@uztdxgw@uU3Eb7tcL_HmbUWNfYnK1U3i_ybqTYDND6fTnVwVNXnNOonND63i_ybqT7rEb73cx6JERVCEnzbd2yvuLk3gm7HluU3mLgDl4VHEmYWp1P3mnV3cWVtc_73pmF3AMst8n8vqRYfqCV3MOFtARgbBxXSal@SRDgb8x@SmpzDK1U3i_ybqTYDNOMDdf8fGuNtqhQwuNztcT7r3nV39NVwc_7rDnVwcmzwp_7raAFHAigbmRsvE_6HdTFvyNUvpxVr8fzDND63i_ybqT7rEb73cxXrERVCEnzbd2yvuLk3gm7HTIXnGuzHd_7romFtqm8DG1_3pm7rKW7rOxNWNuPromFtqNP39L7byoNJubVHcbQwlDPruQXjhM6jzbUWNuPromFtqNP39L7byoNJ8bktWbVwlDPrqf2xQOMrG1_3pmYfqRF3yCU0luFtqRYtBRk3um2wmbQYlDPrqf2xQOMrG1_3pmYfqRF3yCU0ligw@hgCWRVHaRgwAAPfGu@OgoXnGuUOqnV3AuyHuCVxOAPwc2gv9WVHlDPrRhVtuRgOgoXnGuUOqnV3AuyHuCVxOAPwc2gv9WVH3Rk3rhgClDPrqf2xQOMrG1_3pmYfqRF3yCU0liFtqxstuT7odbywmAPfG5gv@LywzbUWNuPry5gHALVHgnktytPrQ0MrGuPrhhk3GuyvGfKrBnsv9xgwATYfi_ywdTywJWgw8RktECUJuLk3gm7HltUWGuyvAiyCqRVrPuUJERVCEnzbd2yvuLk3gm7HloKrqhkfdLyCALVrPuPHmRywQOMrGuPrhhk3GM7rPuPwpLgH8RktENUwcTyz@RgtcNVHu_5CvhswnhgtcCUJuLk3gm7HltU0qfNWGOMrGuPrqhkfu_FvGfKrl1UfihXfqnV3dTs3AIgwEnP3pmYf2LFJQOMrGuPrqhkfpNgwm_Ftmm8DG5gHALVHgnktytPrQ0MrGuPrGuzHd_7ruhVrPuPwpLgH8RktENUvmRgvERgz@RgtcNVHypU3i_ybqTFJgoKruhkfEb73cm8DGpPHcC7HpOgvhhs3i_ybqTFJQuU3dN8vubYtim8DGiY39RsWNuPrGuPrGMyvAMY3im8DGpUfpMkSAuFtqhVwuNztcTFfqnV3AOs3loXnGuPrGuPruNP3d_ywATYopTgwAtktuRk3E_5wRnk3cCU3dWPrubUWNuPrGu84QOMrGuPruNP3d_ywATYopTgwAtktuRk3E_5wRnk3cCP3dWPrubUWNuPrPbPxgoXnK1U3i_ybqTYDND@r8fPr3nV3jTs3AIgwEmPYpmyHATgwmmUXpTgwGlOtBm8f8IXnND63i_ybqT7rEb73cx6JERVCEnzbd2yvuLk3gm7HlIXnhhk3GpstpAVtcTyvlm8DGpstpAVtcTyvlmP4KmUCPZXnlnstlWgwEhswAMgtBm8DGpstpAVtcTyvlNUv8TVrKW7rOxNWN4zw9NsvEbstAC8xGoYnhhk3GpgvBL7rPuPwpLgH8RktENUvmRgvERgz@RgtcNVHypU3i_ybqTFJgoXnlhVwuN8vubYtim8DGiY39RsWNpgvBLYfEb73cm8DGpPHcC7HpOgvhhs3i_ybqTFJQOoHd_7r9Lyw4L_oGfKrl4VHEmF3_pPrPfKrBnsv9xgwATYf@nsvdTybpNkfq_FtEnsvpWsWNpgvBLYfu_FvGfKrylF3cLNY6mUDGpPbET73u06JGOKrl4VHEmYWltPr5uznl1UfaAFHApstpAVtcTyvlLywm2ybiRs3AMst8nPHdAsf2LFflm7HAOs3loXnhhk3GIstBRVrPuPwpLgH8RktENUwcTyz@RgtcNVHu_5CvhswnhgtcCUJuLk3gm7HltU0qfNWNIstBRkfqhk3cNVHnnVwcN8bALywmTYXc2stmRVxlhVwuWPrAnVwcbUWNfyxytUWND6fuLk3gm7HLOonKMFvmbV3EmPHVmywPpPHcC7HpOgvhhs3i_ybqTFJLO1wpnsw@RVHdAkfixVwAuyHuCVxRRYtiTybpNVxguUCNpstpAVtcTyvlNPwc2gbARsY@nVHypUfup6jq5Kjh18S7h6J@uU0eDPref_fGpPwg2yflm7H8aVw8aKjqa@Smp@jqlKW74@fqp8xAaVwBL2wm2ybiRVxlnstlWgwEhswAuyHThVwuC8xgoXnlnstlWgwEhswAuyHThVwuC8xAlktd_VtcL2bAAVtc_2weRywuT7xgoXnlnstlWgwEhswAlktd_VtcL2wm2ybiRs3ytUWNfyxQOMDpMFvmbV3ENXnNOMDdf8fGaKCeu8f8IXnKigbhm8bBx6JBbkH8pV3Ex8vBx8SEu@SeQ6j9u@j74KW8u6JGM7HVWgwPpUHgTVHy0@SqCFWG4gwgAVbE0@SqCFWlIXnKMFvmbV3EmPHVmywPpPHcC7HpOgvhhs3i_ybqTFJLO1wpnsw@RVHdAkfixVwAuyHuCVxRRYtiTybpNVxguUCGpstpAVtcTyvlNPwgL73@hgCypPwg2yflm7H8aVw8aKjqa@Smp@jqlKW74@fqp8xQu84goXnK1U3i_ybqTYDND6fBbkHLOonNOMDuLk3gm7HLOMrG4zw9NsvEbstAC8b@M7fpWUw@Q7fdW8tgoybOAUzpnsw@RgXAhVtVTybiLFoT0gwiTFJzxX3Qts0mx2DgZ03zW74RRYtiTybpNVxgoYnGuPxgZ03zN83Pts0mx0feW74Ox2xAuyHuCVxd_Fw9xgwATF3gf7fgZ03zNPtPaXxARsHGi5vERVxgo@vPMYfi_ywdTywJWgw8RktECUtgDznGu8tPMYflRVHJWgw8RktELYXVT2vlN5v8RVxpbU0qfNWdN8vubYtix@SQakfu_FvPpsW8NP3d_ywATYopTgwAtktuRk3E_5wRnk3cC8v@fgxNuPrPbPxabktBnsH@istiRytcNVH@pU3i_ybqTFJ@pUfppFHaNUwpnsw@RgfdNgv@b7HgLs3AMst8n8vAhVtVTybiLYf2LFJ@pUwdA8xQOonGuUwdCUJi_ywdTywlDPrll2X8iXjaiKjqQ6j8a6J@uUJBbk3cLVHmpyvELVbAMst8A8xQOMrGpgvypU3cNVwlDPrluyvlRkHgRsHltUWNOMDpMFvmbV3ENXnND6fyTyt@NKDuLk3gm7HGDgvAAgHdAgwPOgvhhs3i_ybqTYDN5gHALVHgnktGIst4TyvERF3ytPrQ01HgNVwpAYfuTyvERF3PQzrQO13cT7kgxgwpR7HyQztpL_HdTyHuC8xTD8Squ@xQOp4NIst4TyvERF3ytUWND6fuLk3gm7HLl"
		#	final_rtmp=' token=$doregex[tok] pageUrl=http://www.direct2watch.com/ live=1 timeout=10</link>
			un_chtml=get_html(meta,data);
			str_pattern='streamer.*[\'"](.*?)[\'"]'
		else:
			un_chtml=html
			str_pattern='streamer\': \'(.*?)\''
	else:
			un_chtml=page_data
			str_pattern='streamer.*[\'"](.*?)[\'"]'

	if justHtml:
		return un_chtml+'ThisPage['+url+']'
	print str_pattern,un_chtml
	streamer=re.compile(str_pattern).findall(un_chtml)[0] 
	streamer=streamer.replace('\\/','/')
	str_pattern='file[\'"]?: [\'"](.*?)[\'"]'
	file=re.compile(str_pattern).findall(un_chtml)[0].replace('.flv','')
	#print file, un_chtml
	str_pattern='getJSON\(\"(.*?)\"'
	token_url=re.compile(str_pattern).findall(un_chtml)[0] 
	headers=[('Referer',url)]
	token_html=getUrl(token_url,headers=headers)
	str_pattern='token":"(.*)"'
	token=re.compile(str_pattern).findall(token_html)[0] 
	str_pattern='\'flash\', src: \'(.*?)\''
	swf=re.compile(str_pattern).findall(un_chtml)
	if not swf or len(swf)==0:
		str_pattern='flashplayer: [\'"](.*?)[\'"]'
		swf=re.compile(str_pattern).findall(un_chtml)
	swf=swf[0]
	#print streamer
	app=''
	if '1935/' in streamer:
		app=streamer.split('1935/')[1]
		app+=' app='+app
		streamer=streamer.split('1935/')[0]+'1935/'
	final_rtmp='%s%s playpath=%s swfUrl=%s token=%s live=1 timeout=10 pageUrl=%s'%(streamer,app,file,swf,token,url)
	return final_rtmp
	
#print decrypt_vipracing('http://www.direct2watch.com/embedplayer.php?width=653&height=410&channel=10&autoplay=true','http://vipracing.tv/channel/espn')
