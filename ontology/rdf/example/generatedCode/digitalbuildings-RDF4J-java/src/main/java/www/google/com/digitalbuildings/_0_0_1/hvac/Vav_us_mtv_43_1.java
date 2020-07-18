package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_setpoint;

/**
* Class Vav_us_mtv_43_1 
* Non-standard type for B43
*/
@SuppressWarnings("serial")
public class Vav_us_mtv_43_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Vav_sd_csp implements IVav_us_mtv_43_1{

	IRI newInstance;
	public Vav_us_mtv_43_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_us_mtv_43_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVav_us_mtv_43_1> getAllVav_us_mtv_43_1sObjectsCreated(){
		Set<IVav_us_mtv_43_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_us_mtv_43_1")).subjects().stream()
		.map(mapper->(IVav_us_mtv_43_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}