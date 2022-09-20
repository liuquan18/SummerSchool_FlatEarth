
# --- path to quickplots
path_quickplots = '/home/k/k206175/QuanLiu/SummerSchool_FlatEarth/ens_mean_last50/'

# --- set this to True if the simulation is still running
omit_last_file = True

# --- do ocean and/or atmosphere plots
do_atmosphere_plots = True
do_ocean_plots      = True
do_hamocc_plots     = True

# --- grid information
gname     = 'r2b4_oce_r0004'
lev       = 'L40'
gname_atm = 'r2b3_atm_r0030'
lev_atm   = 'L47'

# --- path to interpolation files
path_grid        = '/work/mh0033/m300602/icon/grids/'+gname+'/'
path_grid_atm    = '/work/mh0033/m300602/icon/grids/'+gname_atm+'/'
path_ckdtree     = path_grid+'/ckdtree/'
path_ckdtree_atm = path_grid_atm+'/ckdtree/'

# --- grid files and reference data
path_pool_oce       = '/pool/data/ICON/oes/input/r0004/icon_grid_0036_R02B04_O/'
gnameu = gname.split('_')[0].upper()
fpath_tgrid         = path_pool_oce + gnameu+'_ocean-grid.nc'
fpath_tgrid_atm     = '/pool/data/ICON/grids/public/mpim/0030/icon_grid_0030_R02B03_G.nc'
fpath_ref_data_oce  = '/pool/data/ICON/oes/input/r0004/icon_grid_0036_R02B04_O/R2B4L40_initial_state.nc'
#fpath_ref_data_atm  = '/work/mh0033/m300602/icon/era/pyicon_prepare_era.nc'
fpath_ref_data_atm  = '/work/mh0033/m300602/icon/era/pyicon_prepare_era.nc'
fpath_fx            = path_grid + gname+'_'+lev+'_fx.nc'

# --- nc file prefixes
D_variable_container = dict(
  default  = '_oce_P1M_3d',
  to       = '_oce_P1M_3d',
  so       = '_oce_P1M_3d',
  u        = '_oce_P1M_3d',
  v        = '_oce_P1M_3d',
  massflux = '_oce_P1M_3d',
  moc      = '_oce_P1M_moc',
  mon      = '_oce_mon',
  ice      = '_oce_P1M_2d',
  monthly  = '_oce_P1M_2d',
  sqr      = '_oce_P1M_sqr',
)

ham_inv = '_hamocc'
ham_2d = '_hamocc_2d_tendencies'
ham_mon = '_hamocc_monitor'

atm_2d = '_atm_2d_ml'
atm_3d = '_atm_3d_ml'
atm_mon = '_atm_mon'

lnd_2d = '_lnd_basic_ml'

tstep_ts  = '????????'
tstep     = '????????'

time_at_end_of_interval = False

red_list = []
# from dwd; does not work for MPI-ICON
red_list += ['ts_pme_gmean']
# uncomment this if ssh_variance is not there
#red_list += ['ssh']
#red_list += ['ssh_variance']
# uncomment this to omit plots which require loading 3D mass_flux
#red_list += ['bstr', 'arctic_budgets', 'passage_transports']
# uncomment this to omit plots which require loading 3D u, v
#red_list += ['arctic_budgets']
# uncomment this to omit plots which require loading 3D density
#red_list += ['dens30w']

