package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
/**
* Class Dmp_ed 
* Exhaust control damper.
*/
public interface IDmp_ed extends IDmp, IEd{

	public IRI iri();

    public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter);

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor();

}