package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status_1;
/**
* Class Cdws_us_mtv_2081_1 
* Non-standard 2081 CDWS
*/
public interface ICdws_us_mtv_2081_1 extends ICdws{

	public IRI iri();

    public void addUsesReturn_water_isolation_valve_status_1 (IReturn_water_isolation_valve_status_1 parameter);

	public Set<IReturn_water_isolation_valve_status_1> getUsesReturn_water_isolation_valve_status_1();

    public void addUsesReturn_water_isolation_valve_status_2 (IReturn_water_isolation_valve_status_2 parameter);

	public Set<IReturn_water_isolation_valve_status_2> getUsesReturn_water_isolation_valve_status_2();

    public void addUsesReturn_water_isolation_valve_status_3 (IReturn_water_isolation_valve_status_3 parameter);

	public Set<IReturn_water_isolation_valve_status_3> getUsesReturn_water_isolation_valve_status_3();

    public void addUsesReturn_water_isolation_valve_status_4 (IReturn_water_isolation_valve_status_4 parameter);

	public Set<IReturn_water_isolation_valve_status_4> getUsesReturn_water_isolation_valve_status_4();

    public void addUsesSupply_water_isolation_valve_status_1 (ISupply_water_isolation_valve_status_1 parameter);

	public Set<ISupply_water_isolation_valve_status_1> getUsesSupply_water_isolation_valve_status_1();

    public void addUsesSupply_water_isolation_valve_status_2 (ISupply_water_isolation_valve_status_2 parameter);

	public Set<ISupply_water_isolation_valve_status_2> getUsesSupply_water_isolation_valve_status_2();

    public void addUsesSupply_water_isolation_valve_status_3 (ISupply_water_isolation_valve_status_3 parameter);

	public Set<ISupply_water_isolation_valve_status_3> getUsesSupply_water_isolation_valve_status_3();

    public void addUsesSupply_water_isolation_valve_status_4 (ISupply_water_isolation_valve_status_4 parameter);

	public Set<ISupply_water_isolation_valve_status_4> getUsesSupply_water_isolation_valve_status_4();

}